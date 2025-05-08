# CarZone - Used Car Dealership Web App

A Streamlit-based web application for buying and selling used cars, with features like price estimation, OTP verification, and admin panel.

## Features

- 🚗 Browse and filter car listings
- 💰 Sell your car with OTP verification
- 📊 Get price estimates using ML model
- 👨‍💼 Admin panel for managing listings
- 🔒 Secure OTP-based verification
- 📱 Responsive design

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd carzone
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
The database will be automatically created when you run the application.

5. Add your ML model:
Place your trained model file (`model.pkl`) in the `model/` directory.

## Running the App

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

## Project Structure

```
carzone/
├── app.py              # Main application file
├── pages/             # Streamlit pages
│   ├── Home.py        # Home page
│   ├── Buy.py         # Car listings
│   ├── Sell.py        # Sell car form
│   ├── Estimate.py    # Price estimator
│   └── Admin.py       # Admin panel
├── utils/             # Utility functions
│   ├── otp_sender.py  # OTP functionality
│   ├── dropdowns.py   # Dropdown data
│   ├── db.py          # Database operations
│   └── predictor.py   # Price prediction
├── model/             # ML model
│   └── model.pkl      # Trained model
├── uploads/           # Uploaded files
│   ├── images/        # Car images
│   └── documents/     # RC Book, Insurance
└── carzone.db         # SQLite database
```

## Admin Access

To access the admin panel:
1. Navigate to the Admin page
2. Use the default credentials:
   - Username: admin
   - Password: admin123

**Important:** Change the default admin credentials after first login.

## Security Notes

- The Gmail credentials in `otp_sender.py` should be changed for production use
- Store sensitive information in environment variables
- Use HTTPS in production
- Regularly backup the database

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 