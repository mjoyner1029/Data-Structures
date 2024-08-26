# src/conversation_manager.py
import heapq
from datetime import datetime

class Conversation:
    def __init__(self, conversation_id, last_activity):
        self.conversation_id = conversation_id
        self.last_activity = last_activity

    def __lt__(self, other):
        return self.last_activity > other.last_activity  # Sort by most recent activity

class ConversationManager:
    def __init__(self):
        self.conversations = {}
        self.sorted_conversations = []

    def add_conversation(self, conversation_id, last_activity):
        conv = Conversation(conversation_id, last_activity)
        self.conversations[conversation_id] = conv
        heapq.heappush(self.sorted_conversations, conv)

    def get_active_conversations(self):
        return heapq.nlargest(10, self.sorted_conversations)  # Get top 10 most recent conversations

# Example usage:
if __name__ == "__main__":
    manager = ConversationManager()
    manager.add_conversation(1, datetime.now())
    active_convs = manager.get_active_conversations()
    for conv in active_convs:
        print(f"Conversation ID: {conv.conversation_id}, Last Activity: {conv.last_activity}")
