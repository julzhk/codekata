def start_digit_valid(func):
    def start_digit_validate(postcode):
        '''
        valid post code cannot start with digit 0, 5, 7, 8 or 9
        '''
        if postcode[0] in '05789':
            return False
        return func(postcode)
    return start_digit_validate

def length_valid(func):
    def length_validator(postcode):
        '''
        A valid postcode should be 6 digits
        '''
        MANDITORY_LENGTH = 6
        if len(postcode) != MANDITORY_LENGTH:
            return False
        return func(postcode)
    return length_validator


def only_numbers(func):
    def only_numbers(postcode):
        '''
        A valid postcode should be 6 digits with no white spaces, letters or other symbols.
        '''
        if any([c not in '0123456789' for c in postcode]):
            return False
        return func(postcode)
    return only_numbers

@only_numbers
@length_valid
@start_digit_valid
def zipvalidate(postcode):
    return True


print zipvalidate( '198328' )
print zipvalidate( '310003' )
print zipvalidate( '424000' )

print zipvalidate( '12A483' )
print zipvalidate( '1@63' )
print zipvalidate( '111' )
print zipvalidate( '056879' )
print zipvalidate( '1111111' )