from langchain import agents
from tests.unit_tests import assert_all_importable

EXPECTED_ALL = [
    "Agent",
    "AgentExecutor",
    "AgentExecutorIterator",
    "AgentOutputParser",
    "AgentType",
    "BaseMultiActionAgent",
    "BaseSingleActionAgent",
    "ConversationalAgent",
    "ConversationalChatAgent",
    "LLMSingleActionAgent",
    "MRKLChain",
    "OpenAIFunctionsAgent",
    "OpenAIMultiFunctionsAgent",
    "ReActChain",
    "ReActTextWorldAgent",
    "SelfAskWithSearchChain",
    "StructuredChatAgent",
    "Tool",
    "ZeroShotAgent",
    "create_gigachat_functions_agent",
    "create_json_agent",
    "create_openapi_agent",
    "create_pbi_agent",
    "create_pbi_chat_agent",
    "create_spark_sql_agent",
    "create_sql_agent",
    "create_vectorstore_agent",
    "create_vectorstore_router_agent",
    "get_all_tool_names",
    "initialize_agent",
    "load_agent",
    "load_huggingface_tool",
    "load_tools",
    "tool",
    "XMLAgent",
    "create_openai_functions_agent",
    "create_xml_agent",
    "create_react_agent",
    "create_openai_tools_agent",
    "create_self_ask_with_search_agent",
    "create_json_chat_agent",
    "create_structured_chat_agent",
]


def test_all_imports() -> None:
    assert set(agents.__all__) == set(EXPECTED_ALL)
    assert_all_importable(agents)
