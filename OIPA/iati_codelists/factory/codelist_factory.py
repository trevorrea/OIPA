
# TODO: separate files per logical element (as represented in the API)
# TODO: also, separate for codelists
import iati 
from iati_codelists import models as codelist_models
from iati_vocabulary import models as vocabulary_models

from factory import SubFactory, RelatedFactory
from factory.django import DjangoModelFactory

class NoDatabaseFactory(DjangoModelFactory):
    @classmethod
    def _setup_next_sequence(cls):
        return 0

class GetOrCreateMetaMixin():
    django_get_or_create = ('code',)

class VersionFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = codelist_models.Version

    code = '2.01'
    name = 'IATI version 2.01'

class LanguageFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.Language
        django_get_or_create = ('code',)

    code = 'fr'
    name = 'french'

class FileFormatFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.FileFormat

    code = 'application/json'
    name = ''

class DocumentCategoryCategoryFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.DocumentCategoryCategory

    code = 'A'
    name = 'Activity Level'

class DocumentCategoryFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.DocumentCategory

    code = 'A04'
    name = 'Conditions'
    category = SubFactory(DocumentCategoryCategoryFactory)


class BudgetTypeFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.BudgetType

    code = 1
    name = 'Original'

class ActivityDateTypeFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = codelist_models.ActivityDateType

    code = '1'
    name = 'Planned start'

class CurrencyFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.Currency

    code = 'USD'
    name = 'us dolar'


class CollaborationTypeFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.CollaborationType

    code = 1
    name = 'Bilateral'


class ActivityStatusFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.ActivityStatus

    code = 1
    name = 'Pipeline/identification'


class FlowTypeFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.FlowType

    code = 1
    name = 'test-flowtype'
    description = 'test-flowtype-description'


class AidTypeCategoryFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.AidTypeCategory

    code = 1
    name = 'test-category'
    description = 'test-category-description'


class AidTypeFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.AidType

    code = 1
    name = 'test'
    description = 'test'
    category = SubFactory(AidTypeCategoryFactory)


class DescriptionTypeFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.DescriptionType

    code = "1"
    name = 'General'
    description = 'description here'


class SectorFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.Sector

    code = 200
    name = 'advice'
    description = ''

class SectorCategoryFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.SectorCategory

    code = 200
    name = 'education'
    description = 'education description'

class OrganisationTypeFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.OrganisationType

    code = '10'
    name = 'Government'

class OrganisationRoleFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.OrganisationRole

    code = '1'
    name = 'Funding'

class SectorVocabularyFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = vocabulary_models.SectorVocabulary

    code = "1"
    name = "OECD DAC CRS (5 digit)"

class BudgetIdentifierVocabularyFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = codelist_models.BudgetIdentifierVocabulary

    code = "1"
    name = "IATI"

class BudgetIdentifierFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = codelist_models.BudgetIdentifier

    code = "1"
    name = "IATI"

class PolicyMarkerFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.PolicyMarker

    code = "1"
    name = 'Gender Equality'
class PolicyMarkerVocabularyFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = vocabulary_models.PolicyMarkerVocabulary

    code = "1"
    name = "OECD DAC CRS"

class PolicySignificanceFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.PolicySignificance

    code = "0"
    name = 'not targeted'
    description = 'test description'

class RegionVocabularyFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.RegionVocabulary

    code = "1"
    name = 'test vocabulary'

class FinanceTypeFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.FinanceType

    code = "110"
    name = 'Aid grant excluding debt reorganisation'


class TiedStatusFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.TiedStatus

    code = "3"
    name = 'Partially tied'


class ResultTypeFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.ResultType

    code = "2"
    name = 'ResultType'

class GeographicLocationClassFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.GeographicLocationClass

    code = "2"
    name = 'Populated place'


class GeographicLocationReachFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.GeographicLocationReach

    code = "1"
    name = 'Activity'


class GeographicExactnessFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.GeographicExactness

    code = "1"
    name = 'Exact'


class LocationTypeCategoryFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.LocationTypeCategory

    code = 'S'
    name = 'Spot Features'


class LocationTypeFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.LocationType

    code = 'AIRQ'
    name = 'abandoned airfield'
    description = 'abandoned airfield'
    category = LocationTypeCategoryFactory.build()


class GeographicVocabularyFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.GeographicVocabulary

    code = 'A1'
    name = 'Global Admininistrative Unit Layers'
    description = 'description'

class ActivityScopeFactory(NoDatabaseFactory):
    class Meta(GetOrCreateMetaMixin):
        model = iati.models.ActivityScope

    code = "1"
    name = 'example scope'