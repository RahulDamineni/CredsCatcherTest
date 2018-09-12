import this
import boto

that = 5 * this

try:
    that
except Exception as exc:
    raise(this)

secrets = {
    "dynamoIAMiD": "CGIJZ5AFYCOUKIHAKQF2",
    "dynamoSecretKey": "JEg76iEVPQIS3WIcK2S68Saffu5YEwU3M5Q9dyZe",
}

# These are fake creds, and fake variable names
# Also, fake coding style

boto.resource(**secrets)
