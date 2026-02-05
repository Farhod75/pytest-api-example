from urllib import response
from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
def test_patch_order_by_id():
    create_response = api_helpers.post_api_data("/store/order", {
        "pet_id": 0})
    assert create_response.status_code == 201
    order_id=create_response.json().get("id")


    patch_data = {
        "status": "sold"
    }

    response = api_helpers.patch_api_data(f"/store/order/{order_id}", patch_data)

    # Validate response code
    assert response.status_code == 200

    # Validate response message
    response_data = response.json()
    assert_that(response.json().get("message"), is_("Order and pet status updated successfully"))
