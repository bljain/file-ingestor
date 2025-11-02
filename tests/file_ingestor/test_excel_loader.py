from file_ingestor.excel_loader import ExcelFileLoader


class TestExcelFileLoader:
    def test_validate_file_path_valid(self):
        valid_path = "data/sample.xlsx"
        loader = ExcelFileLoader(file_path=valid_path)
        assert loader.file_path == valid_path

    def test_validate_file_path_invalid(self):
        invalid_path = "data/sample.txt"
        try:
            ExcelFileLoader(file_path=invalid_path)
        except ValueError as e:
            assert str(e) == "file_path must point to a xlsx file"


    def test_load_data_failure(self):
        invalid_file_path = "non_existent_file.xlsx"
        loader = ExcelFileLoader(file_path=invalid_file_path)
        try:
            loader.load_data()
        except RuntimeError as e:
            assert "Failed to load Excel file" in str(e)