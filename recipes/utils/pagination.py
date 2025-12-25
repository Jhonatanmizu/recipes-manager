class Pagination:
    @staticmethod
    def make_pagination_range(
        page_range: list, current_page: int, quantity_pages_to_show: int = 5
    ) -> list[int]:
        half_range = quantity_pages_to_show // 2
        start_index = max(current_page - half_range - 1, 0)
        end_index = start_index + quantity_pages_to_show
        if end_index > len(page_range):
            end_index = len(page_range)
            start_index = max(end_index - quantity_pages_to_show, 0)
        return list(range(page_range[start_index], page_range[end_index - 1] + 1))
