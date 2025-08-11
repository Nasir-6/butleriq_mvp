from supabase import create_client, Client
import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Supabase client
def get_supabase() -> Client:
    """
    Initialize and return a Supabase client.
    """
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("Supabase URL and key must be set in environment variables")
    
    return create_client(url, key)

# Database operations
class Database:
    def __init__(self):
        self.supabase = get_supabase()
    
    async def create_request(self, request_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Create a new request in the database.
        """
        try:
            # Add required fields if not present
            if 'created_at' not in request_data:
                request_data['created_at'] = 'now()'
            if 'updated_at' not in request_data:
                request_data['updated_at'] = 'now()'
                
            response = self.supabase.table('requests').insert(request_data).execute()
            
            # Handle response based on Supabase client version
            if hasattr(response, 'data') and response.data:
                return response.data[0] if isinstance(response.data, list) else response.data
            return None
            
        except Exception as e:
            print(f"Error creating request: {str(e)}")
            return None
    
    async def get_guest_by_room(self, room_number: str) -> Optional[Dict[str, Any]]:
        """
        Get guest information by room number.
        Returns the first checked-in guest in the room.
        """
        try:
            response = (self.supabase.table('guests')
                      .select('*')
                      .eq('room_number', room_number)
                      .eq('status', 'checked_in')
                      .limit(1)
                      .execute())
            
            if hasattr(response, 'data') and response.data:
                return response.data[0] if isinstance(response.data, list) else response.data
            return None
            
        except Exception as e:
            print(f"Error fetching guest: {str(e)}")
            return None
    
    async def create_guest(self, guest_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Create a new guest in the database.
        """
        try:
            # Add required fields if not present
            if 'created_at' not in guest_data:
                guest_data['created_at'] = 'now()'
            if 'updated_at' not in guest_data:
                guest_data['updated_at'] = 'now()'
            if 'status' not in guest_data:
                guest_data['status'] = 'checked_in'
                
            response = self.supabase.table('guests').insert(guest_data).execute()
            
            if hasattr(response, 'data') and response.data:
                return response.data[0] if isinstance(response.data, list) else response.data
            return None
            
        except Exception as e:
            print(f"Error creating guest: {str(e)}")
            return None

# Database instance
db = Database()
