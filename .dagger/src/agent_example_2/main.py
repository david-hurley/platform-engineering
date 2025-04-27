import dagger
from dagger import dag, function, object_type, Secret

@object_type
class AgentExample2:
    @function
    async def ask(
        self,
        db_url: Secret,
        question: str,
    ) -> str:
        print(db_url)
        # create the sql module that we will use to inspect the database
        # sql = dag.SQL(db_url)

        # create an environment for the agent to use
        env = (
            dag.env()
            .with_string_input("question", "what color is the sky", "The question about the database being asked")
            # .with_sql_input("sql", sql, "The SQL module to use to inspect the database")
        )

        # create the agent and run it
        return await (
            dag.llm()
            .with_env(env)
            .with_prompt(
                """You are an expert database administrator. You have been given
a SQL module that already has tools with credentials and the ability to connect to the database to run SQL queries.
Always show the SQL query you used to get the result.

The question is: $question

DO NOT STOP UNTIL YOU HAVE ANSWERED THE QUESTION COMPLETELY."""
            )
            .last_reply()
        ) 


        
