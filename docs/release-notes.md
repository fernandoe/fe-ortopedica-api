# Release Notes

## 0.0.5

- Add models:
    - Making
    - Color
    - Side
    - AmputeeMember
    - AmputationReason
    - TechnicalResponsible
    - Situation
    - AmputationType
    - MoldType
- Add serializers:
    - MakingModelSerializer
    - ColorModelSerializer
    - SideModelSerializer
    - AmputeeMemberModelSerializer
    - AmputationReasonModelSerializer
    - TechnicalResponsibleModelSerializer
    - SituationModelSerializer
    - AmputationTypeModelSerializer
    - MoldTypeModelSerializer
- Add views:
    - MakingModelViewSet
    - ColorModelViewSet
    - SideModelViewSet
    - AmputeeMemberModelViewSet
    - AmputationReasonModelViewSet
    - TechnicalResponsibleModelViewSet
    - SituationModelViewSet
    - AmputationTypeModelViewSet
    - MoldTypeModelViewSet
- Add Django Admin Views
    - Making
    - Color
    - Side
    - AmputeeMember
    - AmputationReason
    - TechnicalResponsible
    - Situation
    - AmputationType
    - MoldType



## 0.0.4

- Integrate with the account service
- Include package: factory-boy==2.11.1
- Add codefactor.io, codacy.com and codebeat.co as a code service



## 0.0.3

- Add support to build on all branches
- Add pre-commit with flake8
- Add ortopedica app
- Add InstitutionModelSerializer, InstitutionModelViewSet
- Add pytest-cov, coverage and coveralls. Configure the https://coveralls.io service



## 0.0.2

- Add kubernetes config files to deploy the app into the dev stack
- Add two initContainers to wait for the mysql and another to run the migrations



## 0.0.1

- Running basic application
