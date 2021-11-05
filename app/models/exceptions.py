class DataNameError(Exception):

    incorrect_data = []
    correct_data = ['title', 'author', 'content', 'tags']

    def __init__(self):
        self.message = { 'erro': 'dados inválidos', 
        'wrong_entry': f'{DataNameError.incorrect_data}', 
        'accepted_data': f'{DataNameError.correct_data}'  }
        
        super().__init__(self.message)

    @staticmethod
    def validade_request_names(request):
        request_list = [data for data in request]
        output = True
        for item in request_list:
            if item not in DataNameError.correct_data:
                DataNameError.incorrect_data.append(item)
                output = False
        return output 
