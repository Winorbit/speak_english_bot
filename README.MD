### Speak English bot

Bot for Telegram (Discord?) to speak with ChatGPT using voice-messages


How to setup local env
```
export PROJECT_ID=exploring-ml-in-education \
export SA_TEXT_SPEECH_API=sa-speach-to-text \
export SA_TEXT_SPEECH_KEY_FILENAME=sa-speach-to-text-key.json
```
```
gcloud config set project $PROJECT_ID
```


Create service-account with permissions to Speach-toText API
```
gcloud iam service-accounts create $SA_TEXT_SPEECH_API
```
Add permisions to this account
```
gcloud projects add-iam-policy-binding $PROJECT_ID --member "serviceAccount:$SA_TEXT_SPEECH_API@$PROJECT_ID.iam.gserviceaccount.com" --role "roles/speech.client"
```
Create key for this account on local machine:

```
gcloud iam service-accounts keys create $SA_TEXT_SPEECH_KEY_FILENAME --iam-account=$SA_TEXT_SPEECH_API@$PROJECT_ID.iam.gserviceaccount.com
```
