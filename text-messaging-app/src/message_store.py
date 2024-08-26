# src/message_store.py
from collections import defaultdict
import heapq
from datetime import datetime
from utils import format_timestamp, log_info

class Message:
    def __init__(self, message_id, content, timestamp):
        self.message_id = message_id
        self.content = content
        self.timestamp = timestamp

class MessageStore:
    def __init__(self):
        self.messages = defaultdict(list)
        self.message_ids = {}

    def add_message(self, conversation_id, message):
        self.messages[conversation_id].append(message)
        self.message_ids[message.message_id] = message
        log_info(f"Message added: ID={message.message_id}, Content={message.content}")

    def get_messages(self, conversation_id):
        return sorted(self.messages[conversation_id], key=lambda msg: msg.timestamp)

    def get_message_by_id(self, message_id):
        return self.message_ids.get(message_id, None)
