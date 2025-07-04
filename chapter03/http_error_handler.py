def get_http_error(error_code):
   error_messages = {
       200: "OK",
       400: "Bad Request",
       404: "Not found"
   }
   return error_messages.get(error_code, "Unknow error.")

def main():
    error_code = 404
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()