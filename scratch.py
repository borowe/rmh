## Changing the windows execution policy so you can run scripts
## https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7

## See current execution policy
# Get-ExecutionPolicy -List

## Change execution policy
# Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser
