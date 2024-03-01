from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('aboutUs/', aboutUsPageView.as_view(), name="quienesSomos"),
    path('noticePrivacy/', NoticePrivacyPageView.as_view(), name="avisoPrivacidad"),
    path('businessCredit/', BusinessCreditPageView.as_view(), name="creditoEmpresarial"),
    path('mortgage/', MortgagePageView.as_view(), name="hipotecario"),
    path('termsConditions/', TermsConditionsCreditPageView.as_view(), name="terminosCondiciones"),
    path('carLoan/', CarLoantPageView.as_view(), name="prestamoAuto"),
    path('insuranceAdvisory/', insuranceAdvisoryPageView.as_view(), name="asesoriaSeguros"),
    path('homeAcquisition/', HomeAcquisitionPageView.as_view(), name="adquisicionVivienda"),
    path('constructionLoan/', ConstructionLoanPageView.as_view(), name="prestamoConstruccion"),
    path('mortgageRefinancing/', MortgageRefinancingPageView.as_view(), name="refinanciamientoHipotecario"),
    path('landAcquisition/', LandAcquisitionPageView.as_view(), name="adquisicionTerreno"),
    path('landAcquisitionConstruction/', LandAcquisitionConstructionPageView.as_view(), name="adquisicionTerrenoConstruccion"),
    path('presale/', PresalePageView.as_view(), name="preventas"),
    path('liquidityLoan/', LiquidityLoanPageView.as_view(), name="prestamoLiquidez"),
    path('mortgageRefinanceLiquidity/', MortgageRefinanceLiquidityPageView.as_view(), name="refinanciamientoHipotecarioLiquidez"),
    path('contact/', ContactPageView.as_view(), name="contacto"),
]