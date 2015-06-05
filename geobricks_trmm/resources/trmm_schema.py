schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "title": "TRMM",
    "description": "TRMM plug-in for Geobricks downloader.",
    "definitions": {
        "href": {
            "title": "Endpoint",
            "description": "Relative path to the service.",
            "type": "string",
            "default": "/"
        },
        "method": {
            "title": "HTTP Method",
            "description": "Method type to invoke the service.",
            "type": "string",
            "enum": [
                "GET",
                "POST",
                "PUT",
                "DELETE"
            ]
        },
        "code": {
            "title": "Code",
            "description": "Encoded value.",
            "type": "string"
        },
        "label": {
            "title": "Label",
            "description": "Human-readable label.",
            "type": "string"
        },
        "code_label": {
            "type": "object",
            "properties": {
                "code": {
                    "$ref": "#/definitions/code"
                },
                "label": {
                    "$ref": "#/definitions/label"
                }
            }
        },
        "layer": {
            "type": "object",
            "properties": {
                "code": {
                    "$ref": "#/definitions/code"
                },
                "label": {
                    "$ref": "#/definitions/label"
                },
                "extensions": {
                    "type": "array",
                    "title": "Extensions",
                    "description": "Extensions available for the same code.",
                    "items": {
                        "type": "string",
                        "title": "Extension",
                        "enum": [
                            ".tif",
                            ".tfw"
                        ]
                    }
                }
            }
        }
    },
    "properties": {
        "service_type": {
            "type": "string",
            "title": "Type",
            "description": "REST service type.",
            "enum": "DATASOURCE",
            "default": "DATASOURCE"
        },
        "list_years": {
            "type": "object",
            "title": "List years",
            "description": "List all the available years.",
            "properties": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "href": {
                            "$ref": "#/definitions/href",
                            "propertyOrder": 0
                        }
                    }
                },
                "target": {
                    "items": {
                        "title": "Year",
                        "$ref": "#/definitions/code_label"
                    },
                    "type": "array"
                }
            }
        },
        "list_months": {
            "type": "object",
            "title": "List months",
            "description": "List all the available months for a given year.",
            "properties": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "href": {
                            "$ref": "#/definitions/href",
                            "propertyOrder": 0
                        },
                        "year": {
                            "type": "integer",
                            "propertyOrder": 1
                        }
                    }
                },
                "target": {
                    "items": {
                        "title": "Month",
                        "$ref": "#/definitions/code_label"
                    },
                    "type": "array"
                }
            }
        },
        "list_days": {
            "type": "object",
            "title": "List days",
            "description": "List all the available days for a given year and month.",
            "properties": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "href": {
                            "$ref": "#/definitions/href",
                            "propertyOrder": 0
                        },
                        "year": {
                            "type": "integer",
                            "propertyOrder": 1
                        },
                        "month": {
                            "type": "integer",
                            "propertyOrder": 2
                        }
                    }
                },
                "target": {
                    "items": {
                        "title": "Day",
                        "$ref": "#/definitions/code_label"
                    },
                    "type": "array"
                }
            }
        },
        "list_layers": {
            "type": "object",
            "title": "List layers",
            "description": "List all the available layers for a given year, month and day.",
            "properties": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "href": {
                            "$ref": "#/definitions/href",
                            "propertyOrder": 0
                        },
                        "year": {
                            "type": "integer",
                            "propertyOrder": 1
                        },
                        "month": {
                            "type": "integer",
                            "propertyOrder": 2
                        },
                        "day": {
                            "type": "integer",
                            "propertyOrder": 3
                        }
                    }
                },
                "target": {
                    "items": {
                        "title": "Layer",
                        "$ref": "#/definitions/layer"
                    },
                    "type": "array"
                }
            }
        }
    }
}
