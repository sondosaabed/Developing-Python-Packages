from impyrial.length.core import inches_to_feet, inches_to_yards

# Define tests for inches_to_feet function
def test_inches_to_feet():
	# Check that 12 inches is converted to 1 foot
    assert inches_to_feet(12) == 1.0
    # Check that 2.5 feet is converted to 30 inches
    assert inches_to_feet(2.5, reverse=True) == 30.0
    
