from mcp.mcp_helper import MCPHelper

#test data

def test_generate_test_data():

    data = MCPHelper.generate_test_data()

    print("\nGenerated Test Data:", data)

    assert "email" in data

    assert "password" in data

    assert data["email"] == "testuser@gmail.com"


#failures can be tested
def test_failure_analysis():

    MCPHelper.analyze_failure(
        "Element not found"
    )

    assert True


#it gives the locator suggestions
def test_locator_suggestion():

    MCPHelper.suggest_locator()

    assert True