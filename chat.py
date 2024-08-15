import os
import base64
from together import Together
import Api as key
def option():
   print( """
             =============================
              Welcome to the world of Al 
             =============================
              There are two types of AI: 
                1: Chatbot
                2: Image AI
             =============================
          """
        )
   user = input("Enter your choice: ")
   if user == "1":
       #chatbot functionality
      def chatbox(query):
         client = Together(api_key=key.apikey)
         response = client.chat.completions.create(
         model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
         messages=[
                 {
                   "role": "user",
                    "content": query
                  },
       
           ],
            max_tokens=512,
            temperature=0.7,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stop=["<|eot_id|>"],
            #stream=True
        )
         print(f"AI: {response.choices[0].message.content}")

      while True:
        q = input("Question: ")
        chatbox(q)
        choice = input(""" 
                       ================================================================
                       If you want to Exit press E, and if you want to Continue press C:
                       ================================================================   """
                       ).strip().upper()
        if choice == 'E':
                print("Exiting Chatbot...")
                break
   elif user == "2":
      # Image AI functionality
      def generate_image(prompt):
         try:
          client = Together(api_key=key.apikey)
          response = client.images.generate(
            prompt=prompt,
            model="stabilityai/stable-diffusion-xl-base-1.0",
            width=1024,
            height=1024,
            steps=40,
            n=1,
            seed=7998
          )
          # Print response for debugging
          #print("Response:", response)
                
          # Check the type of the response
          if hasattr(response, 'data'):
                    image_data = response.data[0].b64_json
          else:
                    # Handle cases where response does not have 'data' attribute
                    raise ValueError("Unexpected response structure.")
          
               # Decode the base64-encoded image data 
          image_bytes = base64.b64decode(image_data)
          with open("generated_image.png", "wb") as f:
                    f.write(image_bytes)
    
          print("Image generated and saved as 'generated_image.png'")
         except Exception as e:
            print(f"An error occurred: {e}")

     # Main loop for generating images
      while True:
        prompt = input("Enter a description for the image: ")

        generate_image(prompt)
        choice = input("""
                       ================================================================
                       If you want to exit press E, and if you want to continue press C:  
                       ================================================================   """
                       ).strip().upper()
        if choice == 'E':
                print("Exiting Image AI...")
                break
       
   else:
        print("Invalid choice. Please enter 1 or 2.")
option()