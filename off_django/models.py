#!/usr/bin/python
# _*_ coding: utf_8 _*_

import datetime
import logging
import openfoodfacts

from tqdm import tqdm

from django.core.exceptions import FieldDoesNotExist
from django.db import models, transaction

from .models_extensions import ListField
from .settings import DATETIME_FORMAT
from .codes_to_country import CODES_TO_COUNTRY


logger = logging.getLogger("django")


class AbstractOFFFood(models.Model):
    """
    Abstract model representing an Open Food Facts food
    """

    class Meta:
        abstract = True

    # General information
    code = models.TextField(default=None, null=True, db_index=True)
    url = models.TextField(default=None, null=True)
    creator = models.TextField(default=None, null=True)
    created_t = models.IntegerField(default=None, null=True)
    created_datetime = models.DateTimeField(default=None, null=True)
    last_modified_t = models.IntegerField(default=None, null=True)
    last_modified_datetime = models.DateTimeField(default=None, null=True)
    product_name = models.TextField(default=None, null=True)
    generic_name = models.TextField(default=None, null=True)
    quantity = models.TextField(default=None, null=True)

    # Tags
    packaging = ListField(default=None, null=True)
    packaging_tags = ListField(default=None, null=True)
    brands = ListField(default=None, null=True)
    brands_tags = ListField(default=None, null=True)
    categories = ListField(default=None, null=True)
    categories_en = ListField(default=None, null=True)
    categories_tags = ListField(default=None, null=True)
    origins = ListField(default=None, null=True)
    origins_tags = ListField(default=None, null=True)
    manufacturing_places = ListField(default=None, null=True)
    manufacturing_places_tags = ListField(default=None, null=True)
    labels = ListField(default=None, null=True)
    labels_en = ListField(default=None, null=True)
    labels_tags = ListField(default=None, null=True)
    emb_codes = models.TextField(default=None, null=True)
    emb_codes_tags = ListField(default=None, null=True)
    first_packaging_code_geo = ListField(default=None, null=True)
    cities = ListField(default=None, null=True)
    cities_tags = ListField(default=None, null=True)
    purchase_places = ListField(default=None, null=True)
    stores = ListField(default=None, null=True)
    countries = ListField(default=None, null=True)
    countries_en = ListField(default=None, null=True)
    countries_tags = ListField(default=None, null=True)

    # Ingredients
    ingredients_text = ListField(default=None, null=True)
    traces = ListField(default=None, null=True)
    traces_en = ListField(default=None, null=True)
    traces_tags = ListField(default=None, null=True)

    # Misc
    additives = ListField(default=None, null=True)
    additives_en = ListField(default=None, null=True)
    additives_n = models.IntegerField(default=None, null=True)
    additives_tags = ListField(default=None, null=True)
    allergens = ListField(default=None, null=True)
    allergens_en = ListField(default=None, null=True)
    image_small_url = models.TextField(default=None, null=True)
    image_url = models.TextField(default=None, null=True)
    image_ingredients_small_url = models.TextField(default=None, null=True)
    image_ingredients_url = models.TextField(default=None, null=True)
    image_nutrition_small_url = models.TextField(default=None, null=True)
    image_nutrition_url = models.TextField(default=None, null=True)
    ingredients_from_palm_oil = ListField(default=None, null=True)
    ingredients_from_palm_oil_n = models.IntegerField(default=None, null=True)
    ingredients_from_palm_oil_tags = ListField(default=None, null=True)
    ingredients_that_may_be_from_palm_oil = ListField(default=None, null=True)
    ingredients_that_may_be_from_palm_oil_n = models.IntegerField(default=None, null=True)
    ingredients_that_may_be_from_palm_oil_tags = ListField(default=None, null=True)
    main_category = models.TextField(default=None, null=True)
    main_category_en = models.TextField(default=None, null=True)
    no_nutriments = models.TextField(default=None, null=True)
    nutrition_grade_fr = models.CharField(max_length=1, default=None, null=True)
    nutrition_grade_uk = models.CharField(max_length=1, default=None, null=True)
    nova_group = models.IntegerField(default=None, null=True)
    pnns_groups_1 = models.TextField(default=None, null=True)
    pnns_groups_2 = models.TextField(default=None, null=True)
    serving_size = models.TextField(default=None, null=True)
    serving_quantity = models.FloatField(default=None, null=True)
    states = ListField(default=None, null=True)
    states_en = ListField(default=None, null=True)
    states_tags = ListField(default=None, null=True)

    # Nutritional facts
    _alpha_linolenic_acid_100g = models.FloatField(default=None, null=True)
    _arachidic_acid_100g = models.FloatField(default=None, null=True)
    _arachidonic_acid_100g = models.FloatField(default=None, null=True)
    _behenic_acid_100g = models.FloatField(default=None, null=True)
    _butyric_acid_100g = models.FloatField(default=None, null=True)
    _capric_acid_100g = models.FloatField(default=None, null=True)
    _caproic_acid_100g = models.FloatField(default=None, null=True)
    _caprylic_acid_100g = models.FloatField(default=None, null=True)
    _cerotic_acid_100g = models.FloatField(default=None, null=True)
    _dihomo_gamma_linolenic_acid_100g = models.FloatField(default=None, null=True)
    _docosahexaenoic_acid_100g = models.FloatField(default=None, null=True)
    _eicosapentaenoic_acid_100g = models.FloatField(default=None, null=True)
    _elaidic_acid_100g = models.FloatField(default=None, null=True)
    _erucic_acid_100g = models.FloatField(default=None, null=True)
    _fructose_100g = models.FloatField(default=None, null=True)
    _gamma_linolenic_acid_100g = models.FloatField(default=None, null=True)
    _glucose_100g = models.FloatField(default=None, null=True)
    _gondoic_acid_100g = models.FloatField(default=None, null=True)
    _lactose_100g = models.FloatField(default=None, null=True)
    _lauric_acid_100g = models.FloatField(default=None, null=True)
    _lignoceric_acid_100g = models.FloatField(default=None, null=True)
    _linoleic_acid_100g = models.FloatField(default=None, null=True)
    _maltodextrins_100g = models.FloatField(default=None, null=True)
    _maltose_100g = models.FloatField(default=None, null=True)
    _mead_acid_100g = models.FloatField(default=None, null=True)
    _melissic_acid_100g = models.FloatField(default=None, null=True)
    _montanic_acid_100g = models.FloatField(default=None, null=True)
    _myristic_acid_100g = models.FloatField(default=None, null=True)
    _nervonic_acid_100g = models.FloatField(default=None, null=True)
    _oleic_acid_100g = models.FloatField(default=None, null=True)
    _palmitic_acid_100g = models.FloatField(default=None, null=True)
    _stearic_acid_100g = models.FloatField(default=None, null=True)
    _sucrose_100g = models.FloatField(default=None, null=True)
    alcohol_100g = models.FloatField(default=None, null=True)
    beta_carotene_100g = models.FloatField(default=None, null=True)
    beta_glucan_100g = models.FloatField(default=None, null=True)
    bicarbonate_100g = models.FloatField(default=None, null=True)
    biotin_100g = models.FloatField(default=None, null=True)
    caffeine_100g = models.FloatField(default=None, null=True)
    calcium_100g = models.FloatField(default=None, null=True)
    carbohydrates_100g = models.FloatField(default=None, null=True)
    carbon_footprint_100g = models.FloatField(default=None, null=True)
    carnitine_100g = models.FloatField(default=None, null=True)
    casein_100g = models.FloatField(default=None, null=True)
    chloride_100g = models.FloatField(default=None, null=True)
    chlorophyl_100g = models.FloatField(default=None, null=True)
    cholesterol_100g = models.FloatField(default=None, null=True)
    choline_100g = models.FloatField(default=None, null=True)
    chromium_100g = models.FloatField(default=None, null=True)
    cocoa_100g = models.FloatField(default=None, null=True)
    collagen_meat_protein_ratio_100g = models.FloatField(default=None, null=True)
    copper_100g = models.FloatField(default=None, null=True)
    energy_100g = models.FloatField(default=None, null=True)
    energy_from_fat_100g = models.FloatField(default=None, null=True)
    fat_100g = models.FloatField(default=None, null=True)
    fiber_100g = models.FloatField(default=None, null=True)
    fluoride_100g = models.FloatField(default=None, null=True)
    folates_100g = models.FloatField(default=None, null=True)
    fruits_vegetables_nuts_100g = models.FloatField(default=None, null=True)
    fruits_vegetables_nuts_estimate_100g = models.FloatField(default=None, null=True)
    glycemic_index_100g = models.FloatField(default=None, null=True)
    inositol_100g = models.FloatField(default=None, null=True)
    iodine_100g = models.FloatField(default=None, null=True)
    iron_100g = models.FloatField(default=None, null=True)
    magnesium_100g = models.FloatField(default=None, null=True)
    manganese_100g = models.FloatField(default=None, null=True)
    molybdenum_100g = models.FloatField(default=None, null=True)
    monounsaturated_fat_100g = models.FloatField(default=None, null=True)
    nucleotides_100g = models.FloatField(default=None, null=True)
    nutrition_score_fr_100g = models.FloatField(default=None, null=True)
    nutrition_score_uk_100g = models.FloatField(default=None, null=True)
    omega_3_fat_100g = models.FloatField(default=None, null=True)
    omega_6_fat_100g = models.FloatField(default=None, null=True)
    omega_9_fat_100g = models.FloatField(default=None, null=True)
    pantothenic_acid_100g = models.FloatField(default=None, null=True)
    ph_100g = models.FloatField(default=None, null=True)
    phosphorus_100g = models.FloatField(default=None, null=True)
    phylloquinone_100g = models.FloatField(default=None, null=True)
    polyols_100g = models.FloatField(default=None, null=True)
    polyunsaturated_fat_100g = models.FloatField(default=None, null=True)
    potassium_100g = models.FloatField(default=None, null=True)
    proteins_100g = models.FloatField(default=None, null=True)
    salt_100g = models.FloatField(default=None, null=True)
    saturated_fat_100g = models.FloatField(default=None, null=True)
    selenium_100g = models.FloatField(default=None, null=True)
    serum_proteins_100g = models.FloatField(default=None, null=True)
    silica_100g = models.FloatField(default=None, null=True)
    sodium_100g = models.FloatField(default=None, null=True)
    starch_100g = models.FloatField(default=None, null=True)
    sugars_100g = models.FloatField(default=None, null=True)
    taurine_100g = models.FloatField(default=None, null=True)
    trans_fat_100g = models.FloatField(default=None, null=True)
    vitamin_a_100g = models.FloatField(default=None, null=True)
    vitamin_b12_100g = models.FloatField(default=None, null=True)
    vitamin_b1_100g = models.FloatField(default=None, null=True)
    vitamin_b2_100g = models.FloatField(default=None, null=True)
    vitamin_b6_100g = models.FloatField(default=None, null=True)
    vitamin_b9_100g = models.FloatField(default=None, null=True)
    vitamin_c_100g = models.FloatField(default=None, null=True)
    vitamin_d_100g = models.FloatField(default=None, null=True)
    vitamin_e_100g = models.FloatField(default=None, null=True)
    vitamin_k_100g = models.FloatField(default=None, null=True)
    vitamin_pp_100g = models.FloatField(default=None, null=True)
    water_hardness_100g = models.FloatField(default=None, null=True)
    zinc_100g = models.FloatField(default=None, null=True)

    @classmethod
    def parse_api_fields(cls, data):
        """
        Parse API fields and return a django ORM ready dict
        """
        treated_fields = {}
        for field in data.keys():
            django_field = field.replace("-", "_")

            value = (data.get(field) or "").strip()

            try:
                field_class = cls._meta.get_field(django_field).__class__
            except FieldDoesNotExist:
                logger.info("A field has been added in Open Food facts and not in off_django : %s" % field)
                continue

            if value == "":
                value = None
            elif field_class == models.FloatField:
                value = float(value)
            elif field_class == models.IntegerField:
                value = int(value)
            elif field_class == models.DateTimeField:
                value = datetime.datetime.strptime(value, DATETIME_FORMAT)
            elif field_class == ListField:
                if " ] [ " in value:
                    value = value.strip("[ ").strip(" ]").split("] [")
                elif ", " in value:
                    value = value.split(", ")
                else:
                    value = value.split(",")

            treated_fields[django_field] = value

        return treated_fields

    @classmethod
    def load(cls, data, create=False):
        """
        Create an OFFFood instance from a dict or return updated existing instance.
        Does not save it

        :param data:        dict        serialization coming from dump
        """
        treated_fields = cls.parse_api_fields(data)

        # instance, created = cls.objects.update_or_create(code=code, defaults=treated_fields)
        if create:
            instance = cls.objects.create(**treated_fields)
        else:
            instances = cls.objects.filter(code=treated_fields.get("code", ""))
            if instances.count() == 0:
                raise Exception("Object update requested but not in DB, use create=True. %s" % data)

            instances.update(**treated_fields)
            instance = instances.first()

        return instance

    def guess_country(self):
        prefix = self.code[:3]

        for boundaries, country in CODES_TO_COUNTRY:
            try:
                code = int(prefix)
            except Exception:
                continue

            if boundaries[0] <= code <= boundaries[1]:
                return country

    def serialize_for_off_api(self):
        """
        Return (json compliant) dict representation of the object ready for post to OFF API
        """

        serialized = {}
        for field in self._meta.get_fields():
            if getattr(self, field.name) is None:
                continue

            key = field.name
            if "_100g" in key:
                key = ("nutriment_%s" % key.replace("_100g", "").replace("_", "-")).replace("_-", "_")

            serialized[key] = getattr(self, field.name)

            if "nutriment_" in key:
                serialized["%s_unit" % key] = "kcal"

        serialized["nutrition_data_per"] = "100g"

        # update serving_size with serving_quantity real value if exists
        if (getattr(self, "serving_quantity") or 0) != 0:
            serialized["serving_size"] = "%sg" % getattr(self, "serving_quantity")

        # Fill country if not already here
        if "countries" not in serialized and (getattr(self, "countries") or []) == []:
            country = self.guess_country()
            if country is not None:
                serialized["countries"] = [country]

        return serialized


class OFFFood(AbstractOFFFood):

    class Meta:
        verbose_name = "OFFFood - Model for Open Food Facts food product"


class AbstractOFFFacet(models.Model):
    """
    Abstract model to manage facets
    Warning : field sameAs has been renamed same_as
    """

    facet_id = models.CharField(max_length=255, primary_key=True, db_index=True)
    name_fr = models.TextField(default=None, null=True)
    name_en = models.TextField(default=None, null=True)
    products = models.IntegerField(default=None, null=True)
    url = models.TextField(default=None, null=True)
    same_as = ListField(default=None, null=True)

    LOCALES = ["fr", "world"]

    class Meta:
        abstract = True

    @classmethod
    def parse_api_fields(cls, data, locale, extra_fields={}):
        """
        Rename and delete fields

        id -> facet_id
        name -> name_XX with XX locale
        """

        locale = locale if locale != "world" else "en"

        if "id" in data:
            data["facet_id"] = data.get("id")
            del data["id"]

        if "name" in data:
            data["name_%s" % locale] = data.get("name")
            del data["name"]

        if "sameAs" in data:
            data["same_as"] = data.get("sameAs")
            del data["sameAs"]

        return data

    @classmethod
    def update_with_off_db(cls, fetch_function):
        """
        Fetch latest info from OFF and update local DB, to be called from
        child class with datasets = {locale: data, ...}
        """
        datasets = {
            locale: fetch_function(locale=locale)
            for locale in cls.LOCALES
        }

        dump = {}
        for locale, dataset in datasets.iteritems():
            for data in dataset:
                additive_info = cls.parse_api_fields(data, locale)
                dump.setdefault(additive_info["facet_id"], {}).update(additive_info)

        dump_ids = set(dump.keys())
        existing_ids = set(list(cls.objects.values_list("facet_id", flat=True)))

        to_create = dump_ids - existing_ids
        to_update = dump_ids - to_create
        to_delete = existing_ids - dump_ids

        with tqdm(total=len(to_create) + len(to_update), unit='it', unit_scale=True) as pbar:
            with transaction.atomic():
                cls.objects.filter(facet_id__in=to_delete).delete()

                for facet_id in to_create:
                    cls.objects.create(**dump.get(facet_id))
                    pbar.update(1)
                for facet_id in to_update:
                    cls.objects.filter(facet_id=facet_id).update(**dump.get(facet_id))
                    pbar.update(1)

    @classmethod
    def fetch_all_facets(cls):
        MODELS = [
            OFFAdditive, OFFAllergen, OFFBrand, OFFCategory, OFFCountry, OFFIngredient,
            OFFLanguage, OFFPackaging, OFFPackagingCode, OFFPurchasePlace, OFFStore,
            OFFTrace, OFFState
        ]
        for MODEL in MODELS:
            logger.info("Fetching %s data" % MODEL.__name__)
            MODEL.update_with_off_db()


class OFFAdditive(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFAdditive - Model for Open Food Facts facet additive"

    @classmethod
    def update_with_off_db(cls):
        super(OFFAdditive, cls).update_with_off_db(openfoodfacts.facets.get_additives)


class OFFAllergen(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFAllergen - Model for Open Food Facts facet allergen"

    @classmethod
    def update_with_off_db(cls):
        super(OFFAllergen, cls).update_with_off_db(openfoodfacts.facets.get_allergens)


class OFFBrand(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFBrand - Model for Open Food Facts facet band"

    @classmethod
    def update_with_off_db(cls):
        super(OFFBrand, cls).update_with_off_db(openfoodfacts.facets.get_brands)


class OFFCategory(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFCategory - Model for Open Food Facts facet category"

    @classmethod
    def update_with_off_db(cls):
        super(OFFCategory, cls).update_with_off_db(openfoodfacts.facets.get_categories)


class OFFCountry(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFCountry - Model for Open Food Facts facet country"

    @classmethod
    def update_with_off_db(cls):
        super(OFFCountry, cls).update_with_off_db(openfoodfacts.facets.get_countries)


class OFFIngredient(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFIngredient - Model for Open Food Facts facet ingredient"

    @classmethod
    def update_with_off_db(cls):
        super(OFFIngredient, cls).update_with_off_db(openfoodfacts.facets.get_ingredients)


class OFFLanguage(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFLanguage - Model for Open Food Facts facet language"

    @classmethod
    def update_with_off_db(cls):
        super(OFFLanguage, cls).update_with_off_db(openfoodfacts.facets.get_languages)


class OFFPackaging(AbstractOFFFacet):

    image = models.TextField(default=None, null=True)

    class Meta:
        verbose_name = "OFFPackaging - Model for Open Food Facts facet packaging"

    @classmethod
    def update_with_off_db(cls):
        super(OFFPackaging, cls).update_with_off_db(openfoodfacts.facets.get_packaging)


class OFFPackagingCode(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFPackagingCode - Model for Open Food Facts facet packaging code"

    @classmethod
    def update_with_off_db(cls):
        super(OFFPackagingCode, cls).update_with_off_db(openfoodfacts.facets.get_packaging_codes)


class OFFPurchasePlace(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFPurchasePlace - Model for Open Food Facts facet purchase place"

    @classmethod
    def update_with_off_db(cls):
        super(OFFPurchasePlace, cls).update_with_off_db(openfoodfacts.facets.get_purchase_places)


class OFFStore(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFStore - Model for Open Food Facts facet store"

    @classmethod
    def update_with_off_db(cls):
        super(OFFStore, cls).update_with_off_db(openfoodfacts.facets.get_stores)


class OFFTrace(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFTrace - Model for Open Food Facts facet trace"

    @classmethod
    def update_with_off_db(cls):
        super(OFFTrace, cls).update_with_off_db(openfoodfacts.facets.get_traces)


class OFFState(AbstractOFFFacet):
    class Meta:
        verbose_name = "OFFState - Model for Open Food Facts facet state"

    @classmethod
    def update_with_off_db(cls):
        super(OFFState, cls).update_with_off_db(openfoodfacts.facets.get_states)
