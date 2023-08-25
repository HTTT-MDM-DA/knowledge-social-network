from django.urls import path
from core.controller import AnswerController

urlpatterns = [
    path('get-by-question-id', AnswerController.getAnswersOfQuestion),
    path('', AnswerController.createAnswer),
<<<<<<< HEAD
    path('get-detail-admin/<int:answerId>', AnswerController.getDetailAnswerForAdmin),
    path('get-by-question-id-admin/<int:questionId>', AnswerController.getAnswersOfQuestionForAdmin),
    path('count/<int:questionId>', AnswerController.countAllAnswersByQuestion),
    path('decline/<int:answerId>', AnswerController.declinePendingAnswer),
    path('accept/<int:answerId>', AnswerController.acceptPendingAnswer),
=======
    path('/get-detail-admin/<int:answerId>', AnswerController.getDetailAnswerForAdmin),
    path('/get-by-question-id-admin/<int:questionId>', AnswerController.getAnswersOfQuestionForAdmin),
    path('/count/<int:questionId>', AnswerController.countAllAnswersByQuestion),
    path('/decline/<int:answerId>', AnswerController.declinePendingAnswer),
    path('/accept/<int:answerId>', AnswerController.acceptPendingAnswer),
    path('/automatic-censor', AnswerController.automaticCensorAnswers),
>>>>>>> b246bceae15fbb2da3d77ba02cd27e8b70a5382d

    path('<int:answerId>/evaluation/<int:userId>/create-update', AnswerController.createOrUpdateEvaluation),
    path('<int:answerId>/evaluation/<int:userId>/delete', AnswerController.deleteEvaluation),
]
