# flake8: noqa

from langchain.graphs.networkx_graph import KG_TRIPLE_DELIMITER
from langchain.prompts.prompt import PromptTemplate

_DEFAULT_KNOWLEDGE_TRIPLE_EXTRACTION_TEMPLATE = (
    "Ты сетевой интеллект, помогающий человеку отслеживать тройки знаний"
    " обо всех соответствующих людях, вещах, концепциях и т.д. и интегрировать"
    " их с твоими знаниями, хранящимися в твоих весах,"
    " а также с теми, что хранятся в графе знаний."
    " Извлеки все тройки знаний из текста."
    " Тройка знаний - это предложение, которое содержит субъект, предикат"
    " и объект. Субъект - это описываемая сущность,"
    " предикат - это свойство субъекта, которое описывается,"
    " а объект - это значение свойства.\n\n"
    "ПРИМЕР\n"
    "Это штат в США. Это также номер 1 производитель золота в США.\n\n"
    f"Вывод: (Невада, является, штатом){KG_TRIPLE_DELIMITER}(Невада, находится в, США)"
    f"{KG_TRIPLE_DELIMITER}(Невада, является номером 1 производителем, золота)\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "ПРИМЕР\n"
    "Я иду в магазин.\n\n"
    "Вывод: НЕТ\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "ПРИМЕР\n"
    "О, ха. Я знаю, что Декарт любит ездить на антикварных скутерах и играть на мандолине.\n"
    f"Вывод: (Декарт, любит ездить на, антикварных скутерах){KG_TRIPLE_DELIMITER}(Декарт, играет на, мандолине)\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "ПРИМЕР\n"
    "{text}"
    "Вывод:"
)

KNOWLEDGE_TRIPLE_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["text"],
    template=_DEFAULT_KNOWLEDGE_TRIPLE_EXTRACTION_TEMPLATE,
)
