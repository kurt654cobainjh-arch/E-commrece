from app.models.surpblates_client import supabse

PRODUTS_TABLE = supabse.table('produtos')

def get_all_products():
    """recuperar todos os produtos do banco de dados Supabase."""
    try:
        response = supabase.table(PRODUTS_TABLE).select('*').execute()
        if response.error:
            print(f"Erro ao recuperar produtos: {response.error.message}")
            return []
        return response.data
    except Exception as e:
        print(f"Ocorreu uma exceção: {str(e)}")
        return []  
