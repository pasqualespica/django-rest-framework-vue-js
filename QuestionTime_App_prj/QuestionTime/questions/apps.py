from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    name = 'questions'
    # Override this method in subclasses to run code when Django starts.
    def ready(self):
        import questions.signals
        print("Override QuestionsConfig ... !!! : ) ")


