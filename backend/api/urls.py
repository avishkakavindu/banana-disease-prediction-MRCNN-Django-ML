from django.urls import path
from .api_views import CreateAccount, UserAPIView, HarvestPredictionAPIView, TestAPIView, VarietyListAPIView, \
   VarietyRetrieveAPIView, HarvestPredictionHistoryAPIView, BananaDiseaseMRCNNAPIView, DiseaseAndCureAPIView, \
   DiseasePredictionHistoryAPIView, WateringPlanAPIView, WateringPlanPredictionHistoryAPIView, FertilizerPlanAPIView, \
   FertilizerPlanPredictionHistoryAPIView, ChatBotAPIView, DiseaseAPIView, CureAPIView, DiseaseQuestionnaireAPIView,\
   DiseaseQuestionnairePredictionHistoryAPIView

app_name = 'api'

urlpatterns = [
   path('profile/create', CreateAccount.as_view(), name="create_user"),
   path('profile', UserAPIView.as_view(), name="profile"),

   # variety related paths
   path('banana-variety/all', VarietyListAPIView.as_view(), name='variety-list'),
   path('banana-variety/<int:pk>', VarietyRetrieveAPIView.as_view(), name='variety-retrieve'),

   # harvest predictions related paths
   path('harvest/predict', HarvestPredictionAPIView.as_view(), name='harvest_prediction'),
   path('harvest/data', HarvestPredictionAPIView.as_view(), name='harvesting_time'),
   path('harvest/prediction-history', HarvestPredictionHistoryAPIView.as_view(), name='harvest_prediction_history'),

   # image based disease detection - MRCNN related paths
   path('disease/all', DiseaseAPIView.as_view(), name='disease_list'),
   path('disease/<int:pk>', DiseaseAPIView.as_view(), name='disease_detail'),
   path('disease', DiseaseAndCureAPIView.as_view(), name='disease_and_cure'),
   path('disease/detect', BananaDiseaseMRCNNAPIView.as_view(), name='disease_detection_mrcnn'),
   path('disease/prediction-history', DiseasePredictionHistoryAPIView.as_view(), name='disease_prediction_history'),
   path('disease/<int:disease_id>/cure', CureAPIView.as_view(), name='cure_list'),

   # watering plan related paths
   path('watering-plan/predict', WateringPlanAPIView.as_view(), name='watering_plan_prediction'),
   path('watering-plan/prediction-history', WateringPlanPredictionHistoryAPIView.as_view(), name='watering_plan_prediction_history'),

   # fertilizer plan related paths
   path('fertilizer-plan/predict', FertilizerPlanAPIView.as_view(), name='fertilizer_plan_prediction'),
   path('fertilizer-plan/prediction-history', FertilizerPlanPredictionHistoryAPIView.as_view(), name='fertilizer_plan_history'),

   # chatbot related paths
   path('chatbot', ChatBotAPIView.as_view(), name='chatbot'),
   path('disease/questionnaire', DiseaseQuestionnaireAPIView.as_view(), name='disease_questionnaire'),
   path('disease/questionnaire-history', DiseaseQuestionnairePredictionHistoryAPIView.as_view(), name='disease_questionnaire_history'),

   # --- for testing --
   path('tests', TestAPIView.as_view(), name='test')
]
