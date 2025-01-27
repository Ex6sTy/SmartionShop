def test_base_product_abstract_methods():
    with pytest.raises(TypeError):
        BaseProduct("Test", "Test description", 100, 10)
