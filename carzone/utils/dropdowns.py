# Car models data
models = {
    "Maruti": ["Alto", "Swift", "Baleno", "Dzire", "Ertiga", "Vitara Brezza"],
    "Hyundai": ["i10", "i20", "Creta", "Venue", "Verna", "Elantra"],
    "Tata": ["Nexon", "Harrier", "Tiago", "Punch", "Altroz", "Safari"],
    "Honda": ["City", "Amaze", "Jazz", "WR-V", "BR-V"],
    "Toyota": ["Innova", "Fortuner", "Glanza", "Urban Cruiser", "Camry"],
    "Mahindra": ["XUV300", "XUV700", "Bolero", "Thar", "Scorpio", "XUV500"]
}

# Location data
locations = {
    "Gujarat": ["Ahmedabad", "Surat", "Rajkot", "Vadodara", "Gandhinagar"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Thane"],
    "Karnataka": ["Bangalore", "Mysore", "Hubli", "Mangalore", "Belgaum"],
    "Delhi": ["New Delhi", "Dwarka", "Rohini", "Pitampura", "Saket"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Salem", "Tiruchirappalli"]
}

# Other dropdown options
fuel_types = ["Petrol", "Diesel", "CNG", "Electric", "Hybrid"]
transmission_types = ["Manual", "Automatic", "AMT", "CVT", "DCT"]
ownership_types = ["First", "Second", "Third", "Fourth"]
variants = ["LXI", "VXI", "ZXI", "ZXI+", "AMT", "Diesel", "Petrol"]
extra_features = [
    "Sunroof",
    "Rear Camera",
    "Navigation",
    "Alloy Wheels",
    "Touch Screen",
    "Airbags",
    "ABS",
    "Cruise Control",
    "Leather Seats",
    "Climate Control"
]

def get_models_for_maker(maker):
    """Get list of models for a given car maker"""
    return models.get(maker, [])

def get_cities_for_state(state):
    """Get list of cities for a given state"""
    return locations.get(state, []) 