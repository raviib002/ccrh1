from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'ccrh' # Must be replaced by your <storage_account_name>
    account_key = 'LMcqMjpZQUIKkieI8wpEZjCWLT9ciwMafW2NeVjx6Cf7s6StaFRaDZ5ul8zlDNqJdpJec0dhRwPtbPXnWjYyfg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'ccrh' # Must be replaced by your storage_account_name
    account_key = 'LMcqMjpZQUIKkieI8wpEZjCWLT9ciwMafW2NeVjx6Cf7s6StaFRaDZ5ul8zlDNqJdpJec0dhRwPtbPXnWjYyfg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
