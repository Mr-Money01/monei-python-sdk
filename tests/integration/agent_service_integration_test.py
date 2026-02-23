import os
import pytest
import logging
from monei.models.agent import (
    AgentChatRequestDto, AgentStreamRequestDto, GuestAgentRequestDto
)

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestAgentService:

    @pytest.fixture(autouse=True)
    async def _setup(self, agent_service):
        self.client = agent_service
        #self.test_conversation_id = os.getenv("TEST_CONVERSATION_ID", "test-conv-id")
        conversations = await self.client.get_conversations()
        if conversations:
            self.test_conversation_id = conversations[0].id 
            #self.test_conversation_reference = conversations[0].reference

    # ---------------- Read-only endpoints ---------------- #

    async def test_get_conversations(self):
        convs = await self.client.get_conversations()

        #logger.info(f"Conversations: {convs}")
        assert isinstance(convs, list)

    async def test_get_conversation_messages(self):
        messages = await self.client.get_conversation_messages(self.test_conversation_id, limit=5)
        #logger.info(f"Messages: {messages}")
        assert isinstance(messages, list)

    # ---------------- Chat endpoints ---------------- #

    
    async def test_chat(self):
        request = AgentChatRequestDto(
            conversationId=self.test_conversation_id,
            message="Hello, test!"
        )
        response = await self.client.chat(request)
        logger.info(f"Chat response: {response}")
        #assert hasattr(response, "message")

    # ---------------- Conversation management ---------------- #

    
    async def test_initialize_and_delete_conversation(self):
        conv_id = "test-init-delete1"
        init_response = await self.client.initialize_conversation(conv_id)
        logger.info(f"Initialized conversation: {init_response}")
        assert isinstance(init_response, dict)

        await self.client.delete_conversation(conv_id)
        logger.info(f"Deleted conversation: {conv_id}")

    
    async def test_pin_conversation(self):

        messages = await self.client.get_conversation_messages(self.test_conversation_id, limit=5)
        logger.info(f"Messages: {messages}")
        logger.info(f"convo_id: {self.test_conversation_id}")

        
        #assert isinstance(init_response, dict)

        await self.client.pin_conversation(self.test_conversation_id, pin=False)
        #assert pin_msg is None

        # For PATCH operations that return no content
        #self.assertEqual(response.status_code, 204)  # No Content
        # Don't try to parse JSON from empty response
        #self.assertEqual(pin_msg.content, b'')
        #logger.info(f"Pinned conversation: {conv_id}")

        #unpin_msg = await self.client.pin_conversation(conv_id, pin=False)
        #logger.info(f"Unpinned conversation: {conv_id}")

    # ---------------- Stream endpoints (mock/response check) ---------------- #

   
    async def test_stream_chat(self):
        request = AgentStreamRequestDto(
            conversationId=self.test_conversation_id,
            message="Streaming test"
        )
        #initialize first then stream
        response = await self.client.stream_chat(request)
        logger.info(f"Stream chat response: {response}")
        assert isinstance(response, dict)

    @pytest.mark.skipif(
        not os.getenv("ENABLE_AGENT_GUEST_STREAM_TESTS"),
        reason="Guest stream tests disabled"
    )
    async def test_guest_chat_stream(self):
        request = GuestAgentRequestDto(
            guest_id="guest-test",
            message="Guest streaming test"
        )
        response = await self.client.guest_chat_stream(request)
        logger.info(f"Guest stream response: {response}")
        assert isinstance(response, dict)
