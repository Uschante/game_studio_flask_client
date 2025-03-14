## How to install

# Step 1 
Create .env file in src/
# Step 2
Add OPENAI_API_KEY='here is your key' to .env
# Step 3
Install python dependencies from requirements.txt

You can use conda to create a new environment:

```
conda create --name dorf_client python=3.13
conda activate dorf_client
pip3 install -r requirements.txt 
```

# Step 4

Before you started the game itself, run the flask client

In Terminal inside of src/ run:

`flask run`

# Step 5

Run the game
