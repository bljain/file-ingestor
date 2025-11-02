from file_ingestor.csv_loader import CsvFileLoader


class TestCsvFileLoader:
    
    def test_validate_file_path_valid(self):
        valid_path = "data/sample.csv"
        loader = CsvFileLoader(file_path=valid_path)
        assert loader.file_path == valid_path

    def test_validate_file_path_invalid(self):
        invalid_path = "data/sample.txt"
        try:
            CsvFileLoader(file_path=invalid_path)
        except ValueError as e:
            assert str(e) == "file_path must point to a CSV file"

    def test_load_data_success(self, tmp_path):
        # Create a temporary CSV file
        csv_content = "col1,col2\n1,2\n3,4"
        csv_file = tmp_path / "test.csv"
        csv_file.write_text(csv_content)

        loader = CsvFileLoader(file_path=str(csv_file), header=True)
        df = loader.load_data()

        assert not df.empty
        assert list(df.columns) == ["col1", "col2"]
        assert len(df) == 2

    def test_load_data_failure(self):
        invalid_file_path = "non_existent_file.csv"
        loader = CsvFileLoader(file_path=invalid_file_path)
        try:
            loader.load_data()
        except RuntimeError as e:
            assert "Failed to load CSV file" in str(e)