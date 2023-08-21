# flake8: noqa
from langchain.prompts.prompt import PromptTemplate

PROMPT_SUFFIX = """Используй только следующие индексы Elasticsearch:
{indices_info}

Вопрос: {input}
ESQuery:"""

DEFAULT_DSL_TEMPLATE = """Получив входной вопрос, создай синтаксически правильный запрос Elasticsearch для его выполнения. Если пользователь не указывает в своем вопросе конкретное количество примеров, которые он хочет получить, всегда ограничивай свой запрос максимумом {top_k} результатов. Ты можешь упорядочить результаты по релевантной колонке, чтобы вернуть наиболее интересные примеры из базы данных.

Если не указано иное, не запрашивай все колонки из определенного индекса, запрашивай только несколько релевантных колонок, учитывая вопрос.

Обрати внимание, чтобы использовать только имена колонок, которые ты видишь в описании сопоставления. Будь осторожен, чтобы не запрашивать колонки, которые не существуют. Также обрати внимание, какая колонка находится в каком индексе. Верни запрос в виде действительного json.

Используй следующий формат:

Вопрос: Здесь вопрос
ESQuery: Запрос Elasticsearch, отформатированный как json
"""

DSL_PROMPT = PromptTemplate.from_template(DEFAULT_DSL_TEMPLATE + PROMPT_SUFFIX)

DEFAULT_ANSWER_TEMPLATE = """Получив входной вопрос и релевантные данные из базы данных, ответь на вопрос пользователя.

Используй следующий формат:

Вопрос: Здесь вопрос
Данные: Здесь релевантные данные
Ответ: Здесь окончательный ответ

Вопрос: {input}
Данные: {data}
Ответ:"""

ANSWER_PROMPT = PromptTemplate.from_template(DEFAULT_ANSWER_TEMPLATE)
