import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Define car makes and their models with base prices (in lakhs) - Updated 2024 prices from CarDekho/CarWale
car_makes = {
    'Maruti Suzuki': {
        'Alto K10': 3.99,
        'S-Presso': 4.25,
        'Celerio': 5.25,
        'WagonR': 5.54,
        'Swift': 5.99,
        'Baleno': 6.49,
        'Dzire': 6.24,
        'Ciaz': 9.30,
        'Ertiga': 8.69,
        'XL6': 11.29,
        'Vitara Brezza': 8.29,
        'Grand Vitara': 10.70,
        'Fronx': 7.46,
        'Jimny': 12.74,
        'Invicto': 24.79
    },
    'Hyundai': {
        'Grand i10 Nios': 5.73,
        'i20': 7.04,
        'Aura': 6.49,
        'Verna': 11.00,
        'Creta': 11.00,
        'Venue': 7.77,
        'Alcazar': 16.77,
        'Tucson': 28.10,
        'Kona Electric': 23.84,
        'Ioniq 5': 45.95
    },
    'Tata': {
        'Tiago': 5.60,
        'Tigor': 6.30,
        'Altroz': 6.60,
        'Nexon': 8.10,
        'Punch': 6.13,
        'Harrier': 15.49,
        'Safari': 16.19,
        'Nexon EV': 14.74
    },
    'Mahindra': {
        'Bolero': 8.59,
        'Scorpio': 13.59,
        'XUV300': 8.41,
        'XUV400': 15.99,
        'XUV700': 13.99,
        'Thar': 10.98,
        'Bolero Neo': 8.48
    },
    'Toyota': {
        'Glanza': 6.86,
        'Urban Cruiser': 10.86,
        'Innova Crysta': 19.99,
        'Fortuner': 33.43,
        'Vellfire': 1.99,
        'Camry': 46.17,
        'Hilux': 30.40
    },
    'Honda': {
        'Amaze': 7.16,
        'City': 11.16,
        'Elevate': 11.58,
        'WR-V': 8.89
    },
    'Kia': {
        'Seltos': 10.90,
        'Sonet': 7.99,
        'Carens': 10.45,
        'Carnival': 30.99,
        'EV6': 60.97
    },
    'Volkswagen': {
        'Polo': 6.49,
        'Taigun': 11.70,
        'Virtus': 11.56,
        'Tiguan': 35.17
    },
    'Skoda': {
        'Kodiaq': 37.97,
        'Kodiaq Sportline': 39.97,
        'Superb': 34.19,
        'Octavia': 31.45,
        'Kodiaq L&K': 39.97
    },
    'MG': {
        'Astor': 9.98,
        'Comet EV': 7.98,
        'Gloster': 38.80,
        'Hector': 14.00,
        'ZS EV': 22.88
    },
    'Renault': {
        'Kwid': 4.69,
        'Triber': 5.99,
        'Kiger': 6.00
    },
    'Nissan': {
        'Magnite': 6.00,
        'Kicks': 9.50
    },
    'Jeep': {
        'Compass': 20.49,
        'Meridian': 33.60,
        'Wrangler': 60.60,
        'Grand Cherokee': 93.50
    },
    'Mercedes-Benz': {
        'A-Class': 43.80,
        'C-Class': 61.85,
        'E-Class': 63.60,
        'S-Class': 1.70,
        'GLA': 50.50,
        'GLC': 57.40,
        'GLE': 96.40,
        'GLS': 1.32,
        'AMG GT': 2.45
    },
    'BMW': {
        '2 Series': 43.90,
        '3 Series': 47.90,
        '5 Series': 63.40,
        '7 Series': 1.70,
        'X1': 47.90,
        'X3': 62.90,
        'X5': 95.90,
        'X7': 1.78,
        'M3': 1.61,
        'M4': 1.59,
        'M5': 1.61
    },
    'Audi': {
        'A4': 43.19,
        'A6': 63.60,
        'A8 L': 1.57,
        'Q3': 43.81,
        'Q5': 65.18,
        'Q7': 1.14,
        'Q8': 1.14,
        'e-tron': 1.02,
        'RS e-tron GT': 1.95
    },
    'Lexus': {
        'ES': 65.65,
        'LS': 1.81,
        'NX': 71.50,
        'RX': 1.32,
        'LX': 2.32
    },
    'Volvo': {
        'XC40': 45.90,
        'XC60': 65.90,
        'XC90': 1.31
    },
    'Jaguar': {
        'F-Pace': 74.50,
        'I-Pace': 1.05,
        'XF': 71.60
    },
    'Land Rover': {
        'Range Rover': 2.11,
        'Range Rover Sport': 1.63,
        'Range Rover Velar': 1.61,
        'Range Rover Evoque': 67.90,
        'Discovery': 1.36,
        'Discovery Sport': 67.90,
        'Defender': 1.73
    },
    'Porsche': {
        'Macan': 1.65,
        'Cayenne': 1.27,
        'Panamera': 1.63,
        '911': 1.74,
        'Taycan': 1.50
    },
    'Lamborghini': {
        'Huracan': 3.21,
        'Aventador': 6.25,
        'Urus': 4.18
    },
    'Ferrari': {
        'F8': 4.02,
        'SF90': 7.20,
        'Roma': 3.76,
        'Purosangue': 8.80
    },
    'Bentley': {
        'Continental GT': 5.23,
        'Flying Spur': 5.23,
        'Bentayga': 4.10
    },
    'Rolls-Royce': {
        'Ghost': 6.95,
        'Phantom': 9.50,
        'Cullinan': 7.20
    }
}

# Define transmission types
transmission_types = ['Manual', 'Automatic', 'CVT', 'DCT', 'AMT']

# Define states and cities with their price multipliers (based on CarDekho/CarWale data)
locations = {
    'Andhra Pradesh': {
        'cities': ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool', 'Tirupati', 'Kakinada', 'Rajahmundry', 'Kadapa', 'Anantapur'],
        'multiplier': 0.98  # 2% lower
    },
    'Arunachal Pradesh': {
        'cities': ['Itanagar', 'Naharlagun', 'Pasighat', 'Tawang', 'Bomdila', 'Ziro', 'Along', 'Tezu', 'Aalo', 'Daporijo'],
        'multiplier': 0.92  # 8% lower
    },
    'Assam': {
        'cities': ['Guwahati', 'Silchar', 'Dibrugarh', 'Jorhat', 'Nagaon', 'Tinsukia', 'Tezpur', 'Sivasagar', 'Dhubri', 'Diphu'],
        'multiplier': 0.95  # 5% lower
    },
    'Bihar': {
        'cities': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Purnia', 'Darbhanga', 'Arrah', 'Begusarai', 'Katihar', 'Munger'],
        'multiplier': 0.93  # 7% lower
    },
    'Chhattisgarh': {
        'cities': ['Raipur', 'Bhilai', 'Bilaspur', 'Korba', 'Jagdalpur', 'Raigarh', 'Ambikapur', 'Dhamtari', 'Rajnandgaon', 'Durg'],
        'multiplier': 0.96  # 4% lower
    },
    'Delhi NCR': {
        'cities': ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Ghaziabad', 'Mehrauli', 'Shahdara', 'Kalkaji', 'Dwarka', 'Rohini'],
        'multiplier': 1.0  # Base price
    },
    'Goa': {
        'cities': ['Panaji', 'Vasco da Gama', 'Margao', 'Mapusa', 'Ponda', 'Mormugao', 'Sanquelim', 'Bicholim', 'Valpoi', 'Cuncolim'],
        'multiplier': 1.02  # 2% higher
    },
    'Gujarat': {
        'cities': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Jamnagar', 'Bhavnagar', 'Gandhinagar', 'Anand', 'Nadiad', 'Bharuch'],
        'multiplier': 0.97  # 3% lower
    },
    'Haryana': {
        'cities': ['Gurgaon', 'Faridabad', 'Panipat', 'Ambala', 'Yamunanagar', 'Rohtak', 'Hisar', 'Karnal', 'Sonipat', 'Panchkula'],
        'multiplier': 0.99  # 1% lower
    },
    'Himachal Pradesh': {
        'cities': ['Shimla', 'Dharamshala', 'Mandi', 'Solan', 'Kullu', 'Manali', 'Palampur', 'Chamba', 'Bilaspur', 'Una'],
        'multiplier': 0.94  # 6% lower
    },
    'Jharkhand': {
        'cities': ['Ranchi', 'Jamshedpur', 'Dhanbad', 'Bokaro', 'Deoghar', 'Hazaribagh', 'Giridih', 'Ramgarh', 'Medininagar', 'Chatra'],
        'multiplier': 0.93  # 7% lower
    },
    'Karnataka': {
        'cities': ['Bangalore', 'Mysore', 'Hubli', 'Mangalore', 'Belgaum', 'Gulbarga', 'Davanagere', 'Bellary', 'Bijapur', 'Shimoga'],
        'multiplier': 1.05  # 5% higher
    },
    'Kerala': {
        'cities': ['Kochi', 'Thiruvananthapuram', 'Kozhikode', 'Thrissur', 'Kollam', 'Alappuzha', 'Kottayam', 'Palakkad', 'Malappuram', 'Kannur'],
        'multiplier': 1.06  # 6% higher
    },
    'Madhya Pradesh': {
        'cities': ['Indore', 'Bhopal', 'Jabalpur', 'Gwalior', 'Ujjain', 'Sagar', 'Dewas', 'Satna', 'Ratlam', 'Rewa'],
        'multiplier': 0.95  # 5% lower
    },
    'Maharashtra': {
        'cities': ['Mumbai', 'Pune', 'Nagpur', 'Nashik', 'Thane', 'Aurangabad', 'Solapur', 'Amravati', 'Kolhapur', 'Nanded'],
        'multiplier': 1.08  # 8% higher
    },
    'Manipur': {
        'cities': ['Imphal', 'Thoubal', 'Bishnupur', 'Churachandpur', 'Ukhrul', 'Senapati', 'Tamenglong', 'Chandel', 'Jiribam', 'Moreh'],
        'multiplier': 0.92  # 8% lower
    },
    'Meghalaya': {
        'cities': ['Shillong', 'Tura', 'Jowai', 'Nongstoin', 'Williamnagar', 'Baghmara', 'Nongpoh', 'Mairang', 'Resubelpara', 'Khliehriat'],
        'multiplier': 0.93  # 7% lower
    },
    'Mizoram': {
        'cities': ['Aizawl', 'Lunglei', 'Saiha', 'Champhai', 'Kolasib', 'Serchhip', 'Lawngtlai', 'Mamit', 'Saitual', 'Khawzawl'],
        'multiplier': 0.92  # 8% lower
    },
    'Nagaland': {
        'cities': ['Dimapur', 'Kohima', 'Mokokchung', 'Tuensang', 'Wokha', 'Zunheboto', 'Phek', 'Kiphire', 'Longleng', 'Peren'],
        'multiplier': 0.92  # 8% lower
    },
    'Odisha': {
        'cities': ['Bhubaneswar', 'Cuttack', 'Rourkela', 'Berhampur', 'Sambalpur', 'Puri', 'Balasore', 'Bhadrak', 'Baripada', 'Jharsuguda'],
        'multiplier': 0.96  # 4% lower
    },
    'Punjab': {
        'cities': ['Chandigarh', 'Ludhiana', 'Amritsar', 'Jalandhar', 'Patiala', 'Bathinda', 'Moga', 'Muktsar', 'Fatehgarh Sahib', 'Gurdaspur'],
        'multiplier': 0.98  # 2% lower
    },
    'Rajasthan': {
        'cities': ['Jaipur', 'Jodhpur', 'Udaipur', 'Kota', 'Ajmer', 'Bikaner', 'Bharatpur', 'Bhilwara', 'Pali', 'Tonk'],
        'multiplier': 0.95  # 5% lower
    },
    'Sikkim': {
        'cities': ['Gangtok', 'Namchi', 'Mangan', 'Gyalshing', 'Rangpo', 'Singtam', 'Jorethang', 'Ravangla', 'Pelling', 'Lachen'],
        'multiplier': 0.94  # 6% lower
    },
    'Tamil Nadu': {
        'cities': ['Chennai', 'Coimbatore', 'Madurai', 'Salem', 'Tiruchirappalli', 'Tirunelveli', 'Tiruppur', 'Erode', 'Vellore', 'Thoothukudi'],
        'multiplier': 1.03  # 3% higher
    },
    'Telangana': {
        'cities': ['Hyderabad', 'Warangal', 'Karimnagar', 'Nizamabad', 'Khammam', 'Ramagundam', 'Mahbubnagar', 'Nalgonda', 'Siddipet', 'Suryapet'],
        'multiplier': 1.02  # 2% higher
    },
    'Tripura': {
        'cities': ['Agartala', 'Udaipur', 'Dharmanagar', 'Kailashahar', 'Belonia', 'Khowai', 'Teliamura', 'Ambassa', 'Sabroom', 'Kamalpur'],
        'multiplier': 0.93  # 7% lower
    },
    'Uttar Pradesh': {
        'cities': ['Lucknow', 'Kanpur', 'Ghaziabad', 'Agra', 'Varanasi', 'Meerut', 'Allahabad', 'Bareilly', 'Aligarh', 'Moradabad'],
        'multiplier': 0.97  # 3% lower
    },
    'Uttarakhand': {
        'cities': ['Dehradun', 'Haridwar', 'Roorkee', 'Haldwani', 'Rudrapur', 'Kashipur', 'Rishikesh', 'Kotdwara', 'Ramnagar', 'Pithoragarh'],
        'multiplier': 0.96  # 4% lower
    },
    'West Bengal': {
        'cities': ['Kolkata', 'Howrah', 'Durgapur', 'Siliguri', 'Asansol', 'Bardhaman', 'Malda', 'Baharampur', 'Habra', 'Kharagpur'],
        'multiplier': 0.95  # 5% lower
    }
}

def calculate_depreciation(age, km_driven, condition):
    """Calculate depreciation based on age, kilometers, and condition (matching CarDekho/CarWale)"""
    # Base depreciation per year (varies by age)
    if age <= 1:
        yearly_depreciation = 0.15  # 15% in first year (reduced from 25%)
    elif age <= 3:
        yearly_depreciation = 0.12  # 12% in years 2-3 (reduced from 18%)
    elif age <= 5:
        yearly_depreciation = 0.10  # 10% in years 4-5 (reduced from 15%)
    else:
        yearly_depreciation = 0.08  # 8% after 5 years (reduced from 12%)
    
    # Calculate age depreciation
    age_depreciation = 1 - (yearly_depreciation * age)
    
    # Calculate kilometer depreciation (less aggressive for excellent condition)
    km_factor = min(km_driven / 100000, 1.0)
    km_depreciation = 1 - (km_factor * 0.25)  # Max 25% depreciation for high mileage (reduced from 35%)
    
    # Calculate condition multiplier (adjusted for more realistic prices)
    condition_multipliers = {
        'Excellent': 0.98,  # Only 2% reduction for excellent condition (was 8%)
        'Good': 0.85,      # 15% reduction (was 18%)
        'Fair': 0.70,      # 30% reduction (was 35%)
        'Poor': 0.50       # 50% reduction (was 55%)
    }
    
    # Combine all factors
    total_depreciation = age_depreciation * km_depreciation * condition_multipliers[condition]
    return max(total_depreciation, 0.20)  # Minimum 20% of original value (increased from 15%)

def calculate_price(base_price, year, fuel_type, transmission, km_driven, condition, body_style, drive_wheels, state, city, previous_owners):
    """Calculate the final price with all factors considered (matching CarDekho/CarWale)"""
    # Get current year
    current_year = datetime.now().year
    age = current_year - year
    
    # Calculate base depreciation
    depreciation_factor = calculate_depreciation(age, km_driven, condition)
    
    # Apply previous owners multiplier
    previous_owners_multipliers = {
        'First Owner': 1.0,      # No reduction for first owner
        'Second Owner': 0.95,    # 5% reduction for second owner
        'Third Owner': 0.90,     # 10% reduction for third owner
        'Fourth Owner': 0.85,    # 15% reduction for fourth owner
        'Fifth Owner or More': 0.80  # 20% reduction for fifth or more owners
    }
    
    # Apply fuel type multiplier (based on current market trends)
    fuel_multipliers = {
        'Petrol': 1.0,      # Base price
        'Diesel': 1.12,     # Diesel cars are 12% more expensive
        'CNG': 0.92,        # CNG cars are 8% cheaper (about 1 lakh less)
        'Electric': 1.35,   # Electric cars are 35% more expensive (4-5 lakhs more)
        'Hybrid': 1.25      # Hybrid cars are 25% more expensive
    }
    
    # Apply transmission multiplier (based on market preferences)
    transmission_multipliers = {
        'Manual': 1.0,
        'Automatic': 1.15,  # Automatic is more expensive (reduced from 1.20)
        'CVT': 1.12,       # CVT is more expensive (reduced from 1.15)
        'DCT': 1.20,       # DCT is more expensive (reduced from 1.25)
        'AMT': 1.08        # AMT is more expensive (reduced from 1.10)
    }
    
    # Apply body style multiplier (based on market demand)
    body_style_multipliers = {
        'Sedan': 1.0,
        'Hatchback': 0.92,
        'Wagon': 1.08,
        'Hardtop': 1.12,
        'Convertible': 1.18,
        'SUV': 1.15,
        'MPV': 1.10,
        'Truck': 1.25,
        'Van': 1.05,
        'Bus': 1.30,
        'Mini': 0.90,
        'Other': 1.0
    }
    
    # Apply drive wheels multiplier
    drive_wheels_multipliers = {
        'FWD': 1.0,
        'RWD': 1.08,       # Reduced from 1.10
        '4WD': 1.15        # Reduced from 1.18
    }
    
    # Calculate final price
    price = base_price
    price *= fuel_multipliers[fuel_type]
    price *= transmission_multipliers[transmission]
    price *= body_style_multipliers[body_style]
    price *= drive_wheels_multipliers[drive_wheels]
    price *= depreciation_factor
    price *= previous_owners_multipliers[previous_owners]  # Apply previous owners multiplier
    
    # Apply location multiplier
    price *= locations[state]['multiplier']
    
    # Add market adjustment factor (based on age and current market trends)
    if age <= 1:
        market_factor = 1.0  # No adjustment for new cars
    elif age <= 3:
        market_factor = 0.95  # 5% discount for recent models (reduced from 8%)
    elif age <= 5:
        market_factor = 0.90  # 10% discount for older models (reduced from 15%)
    else:
        market_factor = 0.85  # 15% discount for much older models (reduced from 22%)
    
    price *= market_factor
    
    return price

def main():
    # st.set_page_config(layout="wide", page_title="TechCar2 - Car Price Estimator", page_icon="💰")

    # Inject unified CSS for all sections
    st.markdown("""
        <style>
        .tc2-header {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            color: white;
            padding: 32px 24px 24px 24px;
            border-radius: 18px;
            margin-bottom: 32px;
            box-shadow: 0 6px 32px rgba(0,0,0,0.25);
            position: relative;
            overflow: hidden;
        }
        .tc2-header h1 {
            font-size: 44px;
            font-weight: 800;
            margin: 0 0 8px 0;
            letter-spacing: 2px;
            display: flex;
            align-items: center;
        }
        .tc2-header .car-emoji {
            font-size: 48px;
            margin-right: 18px;
            filter: drop-shadow(0 2px 8px #0008);
        }
        .tc2-header p {
            font-size: 20px;
            opacity: 0.92;
            margin: 0;
        }
        .tc2-header::before {
            content: '';
            position: absolute;
            top: -60px; left: -60px;
            width: 200px; height: 200px;
            background: radial-gradient(circle, #4CAF50 0%, transparent 70%);
            opacity: 0.18;
            animation: shine 4s linear infinite;
        }
        @keyframes shine {
            0% { left: -60px; top: -60px; }
            100% { left: 80vw; top: 60px; }
        }
        .tc2-card {
            background: linear-gradient(120deg, #232526 0%, #393939 100%);
            border-radius: 16px;
            box-shadow: 0 2px 16px rgba(0,0,0,0.18);
            padding: 32px 24px;
            margin-bottom: 32px;
            color: white;
            transition: box-shadow 0.3s, transform 0.3s;
        }
        .tc2-card:hover {
            box-shadow: 0 8px 32px rgba(76,175,80,0.18);
            transform: translateY(-2px) scale(1.01);
        }
        .tc2-feature-badge {
            display: inline-block;
            background: linear-gradient(90deg, #43e97b 0%, #38f9d7 100%);
            color: #232323;
            font-size: 18px;
            font-weight: 700;
            border-radius: 10px;
            padding: 6px 18px;
            margin-bottom: 8px;
            box-shadow: 0 2px 8px #38f9d755;
            letter-spacing: 1px;
        }
        .tc2-badge {
            display: inline-block;
            background: linear-gradient(90deg, #43e97b 0%, #38f9d7 100%);
            color: #232323;
            font-size: 28px;
            font-weight: 800;
            border-radius: 10px;
            padding: 10px 28px;
            margin-bottom: 12px;
            box-shadow: 0 2px 8px #38f9d755;
            letter-spacing: 1px;
            animation: pop 0.7s cubic-bezier(.68,-0.55,.27,1.55);
        }
        @keyframes pop {
            0% { transform: scale(0.7); opacity: 0; }
            80% { transform: scale(1.1); opacity: 1; }
            100% { transform: scale(1); }
        }
        .tc2-spec-label {
            color: #b2ffb2;
            font-weight: 600;
            font-size: 16px;
        }
        .tc2-spec-value {
            color: #fff;
            font-size: 16px;
            font-weight: 400;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="tc2-header">
            <h1><span class="car-emoji">💰</span>Car Price Estimator</h1>
            <p>Get an instant, market-based price estimate for your car</p>
        </div>
    """, unsafe_allow_html=True)

    # Card for the input form
    st.markdown("<div class='tc2-card'>", unsafe_allow_html=True)
    st.subheader("Car Details")
    col1, col2 = st.columns(2)
    with col1:
        selected_make = st.selectbox("Car Make", list(car_makes.keys()))
    with col2:
        selected_model = st.selectbox("Car Model", list(car_makes[selected_make].keys()))
    st.subheader("Location")
    col1, col2 = st.columns(2)
    with col1:
        selected_state = st.selectbox("State", list(locations.keys()))
    with col2:
        selected_city = st.selectbox("City", locations[selected_state]['cities'])
    st.subheader("Technical Specifications")
    col1, col2 = st.columns(2)
    with col1:
        year = st.number_input("Year of Manufacture", min_value=1990, max_value=datetime.now().year, value=2020)
        engine_size = st.number_input("Engine Size (cc)", 50, 500, 150)
        horsepower = st.number_input("Horsepower", 30, 300, 100)
    with col2:
        km_driven = st.number_input("Kilometers Driven", min_value=0, value=10000)
        fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Electric', 'Hybrid'])
        body_style = st.selectbox("Body Style", ['Sedan', 'Hatchback', 'Wagon', 'Hardtop', 'Convertible', 'SUV', 'MPV', 'Truck', 'Van', 'Bus', 'Mini', 'Other'])
    col1, col2 = st.columns(2)
    with col1:
        transmission = st.selectbox("Transmission", transmission_types)
    with col2:
        drive_wheels = st.selectbox("Drive Wheels", ['FWD', 'RWD', '4WD'])
    col1, col2 = st.columns(2)
    with col1:
        condition = st.select_slider(
            "Car Condition",
            options=['Excellent', 'Good', 'Fair', 'Poor'],
            value='Good'
        )
    with col2:
        previous_owners = st.selectbox(
            "Number of Previous Owners",
            options=['First Owner', 'Second Owner', 'Third Owner', 'Fourth Owner', 'Fifth Owner or More'],
            help="Select the number of previous owners of the car"
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # Card for the results
    if st.button("Estimate Price", key="est_btn", help="Click to get your car's estimated price", args=None):
        base_price = car_makes[selected_make][selected_model]
        estimated_price = calculate_price(
            base_price=base_price,
            year=year,
            fuel_type=fuel_type,
            transmission=transmission,
            km_driven=km_driven,
            condition=condition,
            body_style=body_style,
            drive_wheels=drive_wheels,
            state=selected_state,
            city=selected_city,
            previous_owners=previous_owners
        )
        st.markdown("<div class='tc2-card' style='background:linear-gradient(120deg,#181818 0%,#232526 100%);margin-top:12px;'>", unsafe_allow_html=True)
        st.markdown(f"<div class='tc2-badge'>₹{estimated_price:.2f} Lakhs</div>", unsafe_allow_html=True)
        st.subheader("Price Estimate")
        price_range = f"Price Range: ₹{estimated_price*0.95:.2f} - ₹{estimated_price*1.05:.2f} Lakhs"
        st.info(price_range)
        location_impact = f"Location Impact: {((locations[selected_state]['multiplier'] - 1) * 100):+.1f}% from base price"
        st.info(location_impact)
        st.subheader("Car Specifications")
        details = {
            "Make": selected_make,
            "Model": selected_model,
            "Location": f"{selected_city}, {selected_state}",
            "Year": year,
            "Engine Size": f"{engine_size} cc",
            "Horsepower": f"{horsepower} hp",
            "Transmission": transmission,
            "Fuel Type": fuel_type,
            "Body Style": body_style,
            "Drive Type": drive_wheels,
            "Kilometers Driven": f"{km_driven:,} km",
            "Condition": condition,
            "Previous Owners": previous_owners
        }
        col1, col2 = st.columns(2)
        for i, (key, value) in enumerate(details.items()):
            if i < len(details) // 2:
                col1.markdown(f"<span class='tc2-spec-label'>{key}:</span> <span class='tc2-spec-value'>{value}</span>", unsafe_allow_html=True)
            else:
                col2.markdown(f"<span class='tc2-spec-label'>{key}:</span> <span class='tc2-spec-value'>{value}</span>", unsafe_allow_html=True)
        st.markdown("<div style='margin-top:18px;'>", unsafe_allow_html=True)
        st.markdown(f"<span class='tc2-feature-badge'>{fuel_type}</span> <span class='tc2-feature-badge'>{body_style}</span> <span class='tc2-feature-badge'>{transmission}</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main() 