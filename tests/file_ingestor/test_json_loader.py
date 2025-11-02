from file_ingestor.json_loader import JsonFileLoader


class TestJsonFileLoader:

    def test_validate_file_path_valid(self):
        valid_path = "data/sample.json"
        loader = JsonFileLoader(file_path=valid_path)
        assert loader.file_path == valid_path

    def test_validate_file_path_invalid(self):
        invalid_path = "data/sample.txt"
        try:
            JsonFileLoader(file_path=invalid_path)
        except ValueError as e:
            assert str(e) == "file_path must point to a JSON file"

    def test_load_data_success(self, tmp_path):
        # Create a temporary JSON file
        json_content = '[{"col1": 1, "col2": 2}, {"col1": 3, "col2": 4}]'
        json_file = tmp_path / "test.json"
        json_file.write_text(json_content)

        loader = JsonFileLoader(file_path=str(json_file), encoding="utf-8")
        df = loader.load_data()

        assert not df.empty
        assert list(df.columns) == ["col1", "col2"]
        assert len(df) == 2

    def test_load_data_failure(self):
        invalid_file_path = "non_existent_file.json"
        loader = JsonFileLoader(file_path=invalid_file_path)
        try:
            loader.load_data()
        except RuntimeError as e:
            assert "Failed to load JSON file" in str(e)