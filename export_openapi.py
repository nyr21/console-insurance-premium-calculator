"""
OpenAPI Schema Export Script

This script exports the OpenAPI (Swagger) schema from the FastAPI application
to a JSON file. This is useful for:
- API documentation
- Client code generation
- Integration with API management tools
- Version control of API specifications

Usage:
    python export_openapi.py
"""

import json
from main import app


def export_openapi_schema(output_file: str = "openapi.json"):
    """
    Export the OpenAPI schema to a JSON file
    
    Args:
        output_file: Name of the output file (default: openapi.json)
    """
    try:
        # Get the OpenAPI schema from the FastAPI app
        openapi_schema = app.openapi()
        
        # Write to file with pretty formatting
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(openapi_schema, f, indent=2, ensure_ascii=False)
        
        print(f"✓ OpenAPI schema successfully exported to '{output_file}'")
        print(f"  - Title: {openapi_schema.get('info', {}).get('title')}")
        print(f"  - Version: {openapi_schema.get('info', {}).get('version')}")
        print(f"  - Endpoints: {len(openapi_schema.get('paths', {}))}")
        
        return True
    
    except Exception as e:
        print(f"✗ Error exporting OpenAPI schema: {str(e)}")
        return False


if __name__ == "__main__":
    print("Insurance Premium Calculator - OpenAPI Schema Export")
    print("=" * 60)
    export_openapi_schema()
