import time
import opal
from pprint import pprint
from opal.api import events_api
from opal.model.paginated_event_list import PaginatedEventList

# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = opal.Configuration(
    host="http://localhost:3000/v1",
    access_token="r69m3gLPr9yq6vL5LJbZZ_rSYqg1r5JPTsQrrXaPBx1egGBNiJtTIJgOng82QaRcY-U6xM2mjIsDlraIKO1xoQ==",
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
# configuration = opal.Configuration(
#     access_token="r69m3gLPr9yq6vL5LJbZZ_rSYqg1r5JPTsQrrXaPBx1egGBNiJtTIJgOng82QaRcY-U6xM2mjIsDlraIKO1xoQ=="
# )


# Enter a context with an instance of the API client
with opal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    start_date_filter = (
        "2024/01/01"  # str | A start date filter for the events. (optional)
    )
    end_date_filter = (
        "2024-01-31"  # str | An end date filter for the events. (optional)
    )
    # actor_filter = "29827fb8-f2dd-4e80-9576-28e31e9934ac"  # str | An actor filter for the events. Supply the ID of the actor. (optional)
    # object_filter = "29827fb8-f2dd-4e80-9576-28e31e9934ac"  # str | An object filter for the events. Supply the ID of the object. (optional)
    # event_type_filter = "29827fb8-f2dd-4e80-9576-28e31e9934ac"  # str | An event type filter for the events. (optional)
    # cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw"  # str | The pagination cursor value. (optional)
    page_size = (
        10  # int | Number of results to return per page. Default is 200. (optional)
    )

    try:
        api_response = api_instance.events(
            start_date_filter=start_date_filter,
            end_date_filter=end_date_filter,
            # actor_filter=actor_filter,
            # object_filter=object_filter,
            # event_type_filter=event_type_filter,
            # cursor=cursor,
            page_size=page_size,
        )
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling EventsApi->events: %s\n" % e)
