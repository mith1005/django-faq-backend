# FAQ Management System with Django

Welcome to the **FAQ Management System** – a complete backend solution for managing FAQs with multilingual support, rich text formatting, and efficient caching! 🚀

---

## Why This Project Rocks! 🌟

Ever wondered how much easier it would be to access a well-organized, multilingual FAQ system? Well, I did more than wonder – I built it! The goal was to design a system that:

- **Supports multiple languages** (English, Hindi, Bengali, and more)
- Uses a **WYSIWYG editor** to allow rich formatting of answers
- Boosts performance with **redis caching** to serve FAQs in the blink of an eye
- Provides a **RESTful API** that delivers FAQs in different languages based on user preferences
- Makes the **admin panel** super easy to use for managing FAQs

In short, this project does it all with great style and performance! 🎯

---

## About Me 🧑‍💻

Yes, I’m that person who can make things happen. If there’s a backend problem, I don’t just solve it – I craft it to perfection. From coding in Django to making sure that each part of the project works seamlessly, I take care of the details that **make me the go-to person for backend roles**. 😉

I’m passionate about coding, problem-solving, and building scalable and clean backend systems. But beyond all that, I **understand people**. I know how to communicate complex things clearly – like this README, where I’ll make sure you see the value I bring to the table.

---

## 🚀 Project Overview

This FAQ Management System project is a perfect blend of backend development skills, including:

- **Django** for managing the backend and APIs
- **django-ckeditor** for rich text editing support
- **Google Translate API** for automating multilingual translation
- **Redis** for caching the FAQ data to boost performance

---

## Features:

1. **Multilingual FAQ Management**  
   FAQs are stored in multiple languages, including English, Hindi, and Bengali. Translations are automatically added via the Google Translate API, allowing seamless internationalization.

2. **WYSIWYG Editor**  
   The answers to the FAQs are rich-text formatted using the **django-ckeditor** library. This allows users to include formatted content, images, and more in their responses.

3. **Efficient Caching with Redis**  
   Redis is integrated to cache FAQ responses. This ensures faster loading times and reduces database queries, improving performance and scalability.

4. **REST API**  
   The project includes a **RESTful API** to fetch FAQs. The API supports dynamic language selection through the `lang` query parameter (e.g., `lang=hi` for Hindi). It also implements caching to avoid redundant API calls.

5. **Admin Interface**  
   FAQs can be easily managed from the Django admin panel. The interface allows you to add, edit, and delete FAQs with ease, making it simple for admins to update content.

---

## Technologies Used 🛠️

- **Django** (Backend framework)
- **django-ckeditor** (WYSIWYG editor integration)
- **googletrans** (Google Translate API for translations)
- **Redis** (Caching mechanism)
- **SQLite** (Database for storing FAQs)
- **Docker** (For containerization)
- **pytest** (Testing framework)

---

## How to Run the Project Locally 🏃‍♂️

1. Clone this repository:
   ```bash
   git clone https://github.com/mith1005/faq_project.git
   cd faq_project

## Create a virtual environment:
      python -m venv venv

## Activate the virtual environment:

### On Windows:
      venv\Scripts\activate

### On Mac/Linux:
      source venv/bin/activate

## Install the dependencies:
      pip install -r requirements.txt

## Set up Redis:

- Ensure Redis is running on your local machine.
- If you haven't installed Redis yet, download and install Redis.

## Apply migrations:
      python manage.py migrate

## Create a superuser (if you want to access the Django admin panel):
      python manage.py createsuperuser

## Run the server:
      python manage.py runserver

- Visit http://127.0.0.1:8000 to access the project and http://127.0.0.1:8000/admin to access the admin panel.

---

## API Endpoints

### GET /api/faqs/
Fetch a list of all FAQs.

#### Example Request:
      curl http://localhost:8000/api/faqs/

#### Example Response:
[
    {
        "question": "What is BharatFD?",
        "answer": "BharatFD is a company dedicated to providing top notch FD services in India."
    },
    ...
]

### GET /api/faqs/?lang=hi
Fetch FAQs in Hindi.

#### Example Request:
      curl http://localhost:8000/api/faqs/?lang=hi

---

## Tests 🧪

This project includes unit tests to ensure everything works as expected. To run the tests, use the following command:

pytest

---

## Future Improvements 🚀

While the project is already feature-rich, here are some improvements I plan to implement in the future:

- Support for more languages.
- Pagination for API responses.
- User authentication and permissions for managing FAQs.

---

## Contributing 🤝

If you want to contribute to this project, feel free to fork the repository and open a pull request. You can also open issues to suggest improvements or report bugs.

Please make sure to follow the conventional commit messages format:

- feat: Add new features.
- fix: Fix issues or bugs.
- docs: Update documentation.

---

## License 📜

This project is open-source and available under the MIT License.

---

## Conclusion 🎉

So, what are you waiting for? Dive into this amazing FAQ Management System, explore the code, and see how I’ve tackled backend challenges with precision, speed, and scalability. I’m confident that this project will be a great addition to any team looking for someone who gets the job done and more. 😉

Let’s connect!
🚀

##SCREENSHOTS

![Screenshot (77)](https://github.com/user-attachments/assets/99214719-b702-4b3d-a80c-11d495f44b73)
![Screenshot 2025-02-02 185339](https://github.com/user-attachments/assets/ff12f05e-e258-402e-a2a4-6e97b8e1ffc1)
![Screenshot 2025-02-02 201127](https://github.com/user-attachments/assets/cdc40eef-7d06-44fa-8f44-3345a906d17b)
![Screenshot 2025-02-02 185545](https://github.com/user-attachments/assets/0108a7c2-d3c8-4b55-bb9e-d5bed44980bb)
![Screenshot 2025-02-02 201323](https://github.com/user-attachments/assets/e8c67e4b-e241-4421-8c35-6c55460964d7)







