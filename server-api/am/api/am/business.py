def auth_user(data):
    username = data.get('username')
    password = data.get('password')

def create_user(data):
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    name = data.get('name')
    user_type = data.get('user_type')
    grade_level = data.get('grade_level')
    mobile = data.get('mobile')
    school_id = data.get('school_id')

def create_school(data):
    name = data.get('name')
    address = data.get('address')
    city = data.get('city')
    state = data.get('state')
    zipcode = data.get('zipcode')
    office_phone_number = data.get('office_phone_number')
    district_id = data.get('district_id')
    school_id = data.get('school_id')
    main_contact_id = data.get('main_contact_id')

def create_activity(data):
    activity_id = data.get('activity_id')
    datetime = data.get('datetime')
    user_id = data.get('user_id')
    activity_type = data.get('activity_type')
    description = data.get('description')
    status = data.get('status')
    lockdown_triggered_by = data.get('lockdown_triggered_by')
    lockdown_triggered_datetime = data.get('lockdown_triggered_datetime')
