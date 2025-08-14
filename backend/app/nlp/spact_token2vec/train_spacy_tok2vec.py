import spacy
from spacy.training.example import Example

from train_data import train_data

# Create blank English pipeline
nlp = spacy.blank("en")

# Add textcat with v3 config format
textcat = nlp.add_pipe(
    "textcat",
    config={
        "model": {
            "@architectures": "spacy.TextCatEnsemble.v2",
            "tok2vec": {
                "@architectures": "spacy.Tok2Vec.v2",
                "embed": {
                    "@architectures": "spacy.MultiHashEmbed.v2",
                    "width": 64,
                    "rows": [2000, 2000, 500, 1000, 500],
                    "attrs": ["NORM", "LOWER", "PREFIX", "SUFFIX", "SHAPE"],
                    "include_static_vectors": False
                },
                "encode": {
                    "@architectures": "spacy.MaxoutWindowEncoder.v2",
                    "width": 64,
                    "window_size": 1,
                    "maxout_pieces": 3,
                    "depth": 2
                }
            },
            "linear_model": {
                "@architectures": "spacy.TextCatBOW.v3",
                "exclusive_classes": True,  # ✅ exclusive_classes is only valid here
                "ngram_size": 1,
                "no_output_layer": False,
                "length": 262144
            }
        }
    }
)

# Add labels
labels = ["Front Desk", "Housekeeping", "Room Service", "Maintenance", "Concierge"]
for label in labels:
    textcat.add_label(label)

# Train
optimizer = nlp.initialize()
for epoch in range(10):
    losses = {}
    for text, annotations in train_data:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], sgd=optimizer, losses=losses)
    print(f"Epoch {epoch} Losses {losses}")

# Save model
nlp.to_disk("hotel_tok2vec")
print("Model saved to hotel_tok2vec")
