import graphene
from graphene_django.types import DjangoObjectType
from .models import (
TbUsers,
TbGroup,
TbGroupUsers,
TbRoles,
TbAccessRights,
TbPOS,
TbAssignPOS,
TbTenderType,
TbTax,
TbTerms,
TbInventoryCategories,
TbAccounts,
TbInventoryAccounts,
TbStores,
TbItemDefinition,
TbInventoryControls,
TbInventoryTransactions,
TbSupplierCategories,
TbSuppliers
)

# First, create a subclass of DjangoObjectType for
# each model you want to query with GraphQL:
class UsersType(DjangoObjectType):
    class Meta:
        model = TbUsers

class GroupType(DjangoObjectType):
    class Meta:
        model = TbGroup

class GroupUsersType(DjangoObjectType):
    class Meta:
        model = TbGroupUsers

class RolesType(DjangoObjectType):
    class Meta:
        model = TbRoles

class AccessRightsType(DjangoObjectType):
    class Meta:
        model = TbAccessRights

class POSType(DjangoObjectType):
    class Meta:
        model = TbPOS

class AssignPOSType(DjangoObjectType):
    class Meta:
        model = TbAssignPOS

class TenderTypeType(DjangoObjectType):
    class Meta:
        model = TbTenderType

class TaxType(DjangoObjectType):
    class Meta:
        model = TbTax

class TermsType(DjangoObjectType):
    class Meta:
        model = TbTerms

class InventoryCategoriesType(DjangoObjectType):
    class Meta:
        model = TbInventoryCategories

class AccountsType(DjangoObjectType):
    class Meta:
        model = TbAccounts

class InventoryAccountsType(DjangoObjectType):
    class Meta:
        model = TbInventoryAccounts

class StoresType(DjangoObjectType):
    class Meta:
        model = TbStores

class ItemDefinitionType(DjangoObjectType):
    class Meta:
        model = TbItemDefinition

class InventoryControlsType(DjangoObjectType):
    class Meta:
        model = TbInventoryControls

class InventoryTransactionsType(DjangoObjectType):
    class Meta:
        model = TbInventoryTransactions

class SupplierCategoriesType(DjangoObjectType):
    class Meta:
        model = TbSupplierCategories

class SuppliersType(DjangoObjectType):
    class Meta:
        model = TbSuppliers



# Next, create an abstract query: a subclass of AbstractType
# (It's abstract because it's an app level query)

# class Query(graphene.AbstractType):
class Query(object):
    # getsingleuser = graphene.Field(UsersType,
    #                           id=graphene.Int(),
    #                           fname=graphene.String())
    getsingleuser = graphene.Field(UsersType, id=graphene.Int())
    all_users = graphene.List(UsersType)
    all_groups = graphene.List(GroupType)
    all_usersgroups = graphene.List(GroupUsersType)
    all_roles = graphene.List(RolesType)
    all_accessrights = graphene.List(AccessRightsType)
    all_pos = graphene.List(POSType)
    all_assignpos = graphene.List(AssignPOSType)
    all_tendertype = graphene.List(TenderTypeType)
    all_taxtype = graphene.List(TaxType)
    all_termstype = graphene.List(TermsType)
    all_inventorycategoriestype = graphene.List(InventoryCategoriesType)
    all_accounttype = graphene.List(AccountsType)
    all_inventoryaccounttype = graphene.List(InventoryAccountsType)
    all_storestype = graphene.List(StoresType)
    all_itemdefinitiontype = graphene.List(ItemDefinitionType)
    all_inventorycontrolstype = graphene.List(InventoryControlsType)
    all_inventorytransactiontype = graphene.List(InventoryTransactionsType)
    all_suppliercategoriestype = graphene.List(SupplierCategoriesType)
    all_suppliertype = graphene.List(SuppliersType)


# You need to create a subclass of graphene.List for each DjangoObjectType then create
# the resolve_xxx() methods for each Query member

    def resolve_all_users(self, context, **kwargs):
        return TbUsers.objects.all()

    def resolve_getsingleuser(self, context, **kwargs):
        id = kwargs.get('id')
        fname = kwargs.get('fname')

        if id is not None:
            return TbUsers.objects.get(pk=id)

        if fname is not None:
            return TbUsers.objects.get(fname=fname)

        return None

    def resolve_all_groups(self, context, **kwargs):
        return TbGroup.objects.all()

    def resolve_all_usersgroup(self, context, **kwargs):
        return TbGroupUsers.objects.all()

    def resolve_all_roles(self, context, **kwargs):
        return TbRoles.objects.all()

    def resolve_all_accessrights(self, context, **kwargs):
        return TbAccessRights.objects.all()

    def resolve_all_pos(self, context, **kwargs):
        return TbPOS.objects.all()

    def resolve_all_assignpos(self, context, **kwargs):
        return TbAssignPOS.objects.all()

    def resolve_all_tendertype(self, context, **kwargs):
        return TbTenderType.objects.all()

    def resolve_all_taxtype(self, context, **kwargs):
        return TbTax.objects.all()

    def resolve_all_termstype(self, context, **kwargs):
        return TbTerms.objects.all()

    def resolve_all_inventorycategoriestype(self, context, **kwargs):
        return TbInventoryCategories.objects.all()

    def resolve_all_accounttype(self, context, **kwargs):
        return TbAccounts.objects.all()

    def resolve_all_inventoryaccounttype(self, context, **kwargs):
        return TbInventoryAccounts.objects.all()

    def resolve_all_storestype(self, context, **kwargs):
        return TbStores.objects.all()

    def resolve_all_itemdefinitiontype(self, context, **kwargs):
        return TbItemDefinition.objects.all()

    def resolve_all_inventorycontrolstype(self, context, **kwargs):
        return TbInventoryControls.objects.all()

    def resolve_all_inventorytransactiontype(self, context, **kwargs):
        return TbInventoryTransactions.objects.all()

    def resolve_all_suppliercategoriestype(self, context, **kwargs):
        return TbSupplierCategories.objects.all()

    def resolve_all_suppliertype(self, context, **kwargs):
        return TbSuppliers.objects.all()
