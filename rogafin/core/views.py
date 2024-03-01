from django.views.generic.base import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "core/index.html"

class aboutUsPageView(TemplateView):
    template_name = "core/aboutUs.html"

class NoticePrivacyPageView(TemplateView):
    template_name = "core/noticePrivacy.html"

class BusinessCreditPageView(TemplateView):
    template_name = "core/businessCredit.html"

class MortgagePageView(TemplateView):
    template_name = "core/mortgage.html"

class TermsConditionsCreditPageView(TemplateView):
    template_name = "core/termsConditions.html"

class CarLoantPageView(TemplateView):
    template_name = "core/carLoan.html"

class insuranceAdvisoryPageView(TemplateView):
    template_name = "core/insuranceAdvisory.html"

class HomeAcquisitionPageView(TemplateView):
    template_name = "core/homeAcquisition.html"

class ConstructionLoanPageView(TemplateView):
    template_name = "core/constructionLoan.html"

class MortgageRefinancingPageView(TemplateView):
    template_name = "core/mortgageRefinancing.html"

class LandAcquisitionPageView(TemplateView):
    template_name = "core/landAcquisition.html"

class LandAcquisitionConstructionPageView(TemplateView):
    template_name = "core/landAcquisitionConstruction.html"

class PresalePageView(TemplateView):
    template_name = "core/presale.html"

class LiquidityLoanPageView(TemplateView):    
    template_name = "core/liquidityLoan.html"

class MortgageRefinanceLiquidityPageView(TemplateView):    
    template_name = "core/mortgageRefinanceLiquidity.html"

class ContactPageView(TemplateView):
    template_name = "core/contact.html"
