def get_mapping(cls):
	mapping = {
	  "@type": {
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "abstract": {
		"type": "text",
		"index": true,
		"copy_to": ["all"]
	  },
	  "alternateName": {
		"type": "text",
		"copy_to": ["all"]
	  },
	  "armGroup": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "name": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "description": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "role": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "intervention": {
			"properties": {
			  "@type": {
				"type": "keyword"
			  },
			  "name": {
				"type": "keyword",
				"copy_to": ["all"]
			  },
			  "category": {
				"type": "keyword",
				"copy_to": ["all"]
			  },
			  "description": {
				"type": "text",
				"copy_to": ["all"]
			  }
			}
		  }
		}
	  },
	  "author": {
		"properties": {
		  "@type": {
			"type": "text"
		  },
		  "affiliation": {
			"properties": {
			  "name": {
				"type": "keyword",
				"copy_to": ["all"]
			  }
			}
		  },
		  "familyName": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "givenName": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "name": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "role": {
			"type": "keyword"
		  },
		  "title": {
			"type": "text"
		  }
		}
	  },
	  "citation": {
		"type": "text"
	  },
	  "citedBy": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "abstract": {
			"type": "text"
		  },
		  "citation": {
			"type": "text"
		  },
		  "datePublished": {
			"type": "text"
		  },
		  "description": {
			"type": "text"
		  },
		  "doi": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "identifier": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "name": {
			"type": "text"
		  },
		  "pmid": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "url": {
			"type": "text"
		  }
		}
	  },
	  "correction": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "correctionType": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "datePublished": {
			"type": "text"
		  },
		  "doi": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "identifier": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "pmid": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "url": {
			"type": "text"
		  }
		}
	  },
	  "creator": {
		"properties": {
		  "@type": {
			"type": "text"
		  },
		  "affiliation": {
			"properties": {
			  "name": {
				"type": "keyword",
				"copy_to": ["all"]
			  }
			}
		  },
		  "familyName": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "givenName": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "name": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "role": {
			"type": "keyword"
		  },
		  "title": {
			"type": "text"
		  }
		}
	  },
	  "curatedBy": {
		"properties": {
		  "@type": {
			"type": "text"
		  },
		  "identifier": {
			"type": "keyword"
		  },
		  "name": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "url": {
			"type": "text"
		  },
		  "versionDate": {
			"type": "keyword"
		  }
		}
	  },
	  "date": {
		"type": "date"
	  },
	  "dateCreated": {
		"type": "keyword"
	  },
	  "dateModified": {
		"type": "keyword"
	  },
	  "datePublished": {
		"type": "keyword"
	  },
	  "description": {
		"type": "text",
		"index": true,
		"copy_to": ["all"]
	  },
	  "distribution": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "contentUrl": {
			"type": "text"
		  },
		  "dateCreated": {
			"type": "keyword"
		  },
		  "dateModified": {
			"type": "keyword"
		  },
		  "datePublished": {
			"type": "keyword"
		  },
		  "description": {
			"type": "text"
		  },
		  "@id": {
			"type": "keyword"
		   },
		  "name": {
			"type": "keyword"
		  }
		}
	  },
	  "doi": {
		"type": "text",
		"copy_to": ["all"]
	  },
	  "duration": {
		"type": "text"
	  },
	  "eligibilityCriteria": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "inclusionCriteria": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "exclusionCriteria": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "minimumAge": {
			"type": "text"
		  },
		  "maximumAge": {
			"type": "text"
		  },
		  "gender": {
			"type": "text"
		  },
		  "healthyVolunteers": {
			"type": "boolean"
		  },
		  "stdAge": {
			"type": "text",
			"copy_to": ["all"]
		  }
		}
	  },
	  "evaluations": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "reviewAspect": {
			"type": "text",
			"copy_to": ["all"]          
		  },
		  "reviewBody": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "author": {
			"properties": {
			  "@type": {
				"type": "text"
			  },
			  "affiliation": {
				"properties": {
				  "name": {
					"type": "keyword",
					"copy_to": ["all"]
				  }
				}
			  },
			  "familyName": {
				"type": "text",
				"copy_to": ["all"]
			  },
			  "givenName": {
				"type": "text",
				"copy_to": ["all"]
			  },
			  "name": {
				"type": "text",
				"copy_to": ["all"]
			  }
			}
		  },
		  "ratingValue": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "ratingExplanation": {
			"type": "text",
			"copy_to": ["all"]
		},
		  "name": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "reviews": {
			"properties": {
			  "@type": {
				"type": "keyword"
			  },
			  "reviewAspect": {
				"type": "text",
				"copy_to": ["all"]          
			  },
			  "author": {
				"properties": {
				  "@type": {
					"type": "text"
				  },
				  "affiliation": {
					"properties": {
					  "name": {
						"type": "keyword",
						"copy_to": ["all"]
					  }
					}
				  },
				  "familyName": {
					"type": "text",
					"copy_to": ["all"]
				  },
				  "givenName": {
					"type": "text",
					"copy_to": ["all"]
				  },
				  "name": {
					"type": "text",
					"copy_to": ["all"]
				  }
				}
			  },
			  "ratingValue": {
				"type": "text",
				"copy_to": ["all"]
			  },
			  "ratingExplanation": {
				"type": "text",
				"copy_to": ["all"]
			  },
			  "name": {
				"type": "text",
				"copy_to": ["all"]
			  },
			  "reviewBody": {
				"type": "text",
				"copy_to": ["all"]
			  },
			  "reviewRating": {
				"properties": {
				  "@type": {
					"type": "keyword"
				  },
				  "reviewAspect": {
					"type": "text",
					"copy_to": ["all"]          
				  },
				  "author": {
					"properties": {
					  "@type": {
						"type": "text"
					  },
					  "affiliation": {
						"properties": {
						  "name": {
							"type": "keyword",
							"copy_to": ["all"]
						  }
						}
					  },
					  "familyName": {
						"type": "text",
						"copy_to": ["all"]
					  },
					  "givenName": {
						"type": "text",
						"copy_to": ["all"]
					  },
					  "name": {
						"type": "text",
						"copy_to": ["all"]
					  }
					}
				  },
				  "ratingValue": {
					"type": "text",
					"copy_to": ["all"]
				  },
				  "ratingExplanation": {
					"type": "text",
					"copy_to": ["all"]
				  },
				  "name": {
					"type": "text",
					"copy_to": ["all"]
				  }            
				}
			  }
			}
		  },
		  "reviewRating": {
			"properties": {
			  "@type": {
				"type": "keyword"
			  },
			  "reviewAspect": {
				"type": "text",
				"copy_to": ["all"]          
			  },
			  "author": {
				"properties": {
				  "@type": {
					"type": "text"
				  },
				  "affiliation": {
					"properties": {
					  "name": {
						"type": "keyword",
						"copy_to": ["all"]
					  }
					}
				  },
				  "familyName": {
					"type": "text",
					"copy_to": ["all"]
				  },
				  "givenName": {
					"type": "text",
					"copy_to": ["all"]
				  },
				  "name": {
					"type": "text",
					"copy_to": ["all"]
				  }
				}
			  },
			  "ratingValue": {
				"type": "text",
				"copy_to": ["all"]
			  },
			  "ratingExplanation": {
				"type": "text",
				"copy_to": ["all"]
			  },
			  "name": {
				"type": "text",
				"copy_to": ["all"]
			  }            
			}
		  }
		}
	  },
	  "funding": {
		"properties": {
		  "funder": {
			"properties": {
			  "name": {
				"type": "keyword",
				"copy_to": ["all"]
			  },
			  "class": {
				"type": "keyword"
			  },
			  "role": {
				"type": "keyword"
			  },
			  "url": {
				"type": "text",
				"copy_to": ["all"]
			  }
			}
		  },
		  "identifier": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "description": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "url": {
			"type": "text",
			"copy_to": ["all"]
		  }
		}
	  },
	  "hasResults": {
		"type": "boolean"
	  },
	  "healthCondition": {
		"type": "text",
		"copy_to": ["all"]
	  },
	  "identifier": {
		"type": "text",
		"copy_to": ["all"]
	  },
	  "identifierSource": {
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "inComplianceWith": {
		"type": "text"
	  },
	  "instrument": {
		"type": "text",
		"copy_to": ["all"]
	  },
	  "interventionText": {
		"type": "text",
		"copy_to": ["all"]
	  },
	  "interventions": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "name": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "category": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "description": {
			"type": "text",
			"copy_to": ["all"]
		  }
		}
	  },
	  "isBasedOn": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "abstract": {
			"type": "text"
		  },
		  "citation": {
			"type": "text"
		  },
		  "datePublished": {
			"type": "text"
		  },
		  "description": {
			"type": "text"
		  },
		  "doi": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "identifier": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "name": {
			"type": "text"
		  },
		  "pmid": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "url": {
			"type": "text"
		  }
		}
	  },
	  "issueNumber": {
		"type": "text"
	  },
	  "journalName": {
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "journalNameAbbrev": {
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "keywords": {
		"type": "keyword",
		"index": true,
		"copy_to": ["all"]
	  },
	  "license": {
		"type": "text"
	  },
	  "material": {
		"type": "text",
		"copy_to": ["all"]
	  },
	  "measurementParameter": {
		"properties": {
		  "resolution": {
			"type": "keyword"
		  }
		}
	  },
	  "measurementTechnique": {
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "name": {
		"type": "keyword",
		"index": true,
		"copy_to": ["all"]
	  },
	  "outcome": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "outcomeMeasure": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "outcomeTimeFrame": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "outcomeType": {
			"type": "keyword",
			"copy_to": ["all"]
		  }
		}
	  },
	  "pmid": {
		"type": "integer",
		"copy_to": ["all"]
	  },
	  "protocolCategory": {
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "protocolSetting": {
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "publicationType": {
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "isRelatedTo": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "abstract": {
			"type": "text"
		  },
		  "citation": {
			"type": "text"
		  },
		  "datePublished": {
			"type": "text"
		  },
		  "description": {
			"type": "text"
		  },
		  "doi": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "identifier": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "name": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "pmid": {
			"type": "text"
		  },
		  "url": {
			"type": "text"
		  }
		}
	  },
	  "infectiousDisease": {
		"normalizer": "keyword_lowercase_normalizer",
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "infectiousAgent": {
		"normalizer": "keyword_lowercase_normalizer",
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "species": {
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "sponsor": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "name": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "class": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "role": {
			"type": "keyword"
		  }
		}
	  },
	  "studyDesign": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "studyType": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "designAllocation": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "studyDesignText": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "designModel": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "designPrimaryPurpose": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "designWhoMasked": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "phase": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "phaseNumber": {
			"type": "half_float"
		  }
		}
	  },
	  "studyEvent": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "studyEventType": {
			"type": "text"
		  },
		  "studyEventDate": {
			"type": "text"
		  },
		  "studyEventDateType": {
			"type": "text"
		  }
		}
	  },
	  "studyLocation": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "name": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "studyLocationCity": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "studyLocationState": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "studyLocationCountry": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "studyLocationStatus": {
			"type": "keyword",
			"copy_to": ["all"]
		  }
		}
	  },
	  "studyStatus": {
		"properties": {
		  "@type": {
			"type": "keyword"
		  },
		  "status": {
			"type": "keyword",
			"copy_to": ["all"]
		  },
		  "statusDate": {
			"type": "text"
		  },
		  "whyStopped": {
			"type": "text",
			"copy_to": ["all"]
		  },
		  "statusExpanded": {
			"type": "boolean"
		  },
		  "enrollmentCount": {
			"type": "integer"
		  },
		  "enrollmentType": {
			"type": "text"
		  }
		}
	  },
	  "topicCategory": {
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "url": {
		"type": "text",
		"copy_to": ["all"]
	  },
	  "usedToGenerate": {
		"type": "text"
	  },
	  "variableMeasured": {
		"type": "keyword",
		"copy_to": ["all"]
	  },
	  "volumeNumber": {
		"type": "text"
	  },
	  "@id": {
		  "type": "keyword"
	  }
	}
	return mapping

