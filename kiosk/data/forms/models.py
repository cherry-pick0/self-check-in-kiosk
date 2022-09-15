from django.db import models

"""
What:
    KioskForm
Attributes:
    kiosk: One kiosk can have one form

Disclaimer: form is very simple
"""


class KioskForm(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""
What:
    FormQuestion
Attributes:
    kiosk_form: One form can have multiple questions
    title: Title of the question
    question_type: Type of a question (input, textarea, select, checkbox)
"""


class FormQuestion(models.Model):

    INPUT = "input"
    TEXTAREA = "textarea"
    SELECT = "select"
    CHECKBOX = "checkbox"
    RADIO = "radio"
    QUESTION_TYPE_CHOICES = (
        (INPUT, "Input"),
        (TEXTAREA, "textarea"),
        (SELECT, "Select"),
        (CHECKBOX, "Checkbox"),
        (RADIO, "Radio"),
    )

    kiosk_form = models.ForeignKey(
        "forms.KioskForm", on_delete=models.CASCADE, null=False
    )
    title = models.CharField(max_length=64, null=False)
    question_type = models.CharField(
        max_length=8, choices=QUESTION_TYPE_CHOICES, default=INPUT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""
What:
    FormAnswer
Attributes:
    kiosk_registration: Registration connected to the answer
    form_question: Question connected to the answer
    value: Value of an answer (text, select, checkbox)

Value answers based on type:

    - input, textarea:
        example: {'input': 'Giraffe'}, {'textarea': 'This text \n breaks here'}

    - checkbox:
        example: {'checkbox': {'Fruit': 'false', 'Veggies': 'true'}}

    - radio, select:
        example: {'radio': 'Fruit'}, {'select': 'Veggies'}
"""


class FormAnswer(models.Model):
    kiosk_registration = models.ForeignKey(
        "registrations.KioskRegistration", on_delete=models.CASCADE, null=False
    )
    form_question = models.ForeignKey(
        "forms.KioskForm", on_delete=models.CASCADE, null=False
    )
    value = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def display_value(self) -> str:
        form_question = FormQuestion.objects.get(id=self.form_question)

        if form_question.question_type in [
            FormQuestion.INPUT,
            FormQuestion.TEXTAREA,
            FormQuestion.RADIO,
            FormQuestion.SELECT,
        ]:
            return self.value.get(form_question.question_type)

        elif form_question.question_type == FormQuestion.CHECKBOX:
            value_list = []
            checkbox_value = self.value.get(FormQuestion.CHECKBOX)

            for key in checkbox_value.keys():
                if checkbox_value.get(key) == "true":
                    value_list.append(key)

            return ", ".join(str(value) for value in value_list)
