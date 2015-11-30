# coursera-data-fetch
using coursera fetch courses, partners and instructors.

```Courses: https://api.coursera.org/api/courses.v1```

	Fields
	
	id: String - The Course Id.
	
	slug: String - The short name associated with the course.
	
	- courseType: CourseType (String) - The type of the course. (e.g. `v1.session`, or `v2.ondemand`, or others)
	
	name: String - The course name or title.
	
	primaryLanguages: Array[String] - The language codes for the course. (e.g. `en` means English.)
	
	subtitleLanguages: Array[String] - The language codes for which subtitles are available.
	
	partnerLogo: Option[String] - If specified, an override logo for the partner for this course.
	
	instructorIds: Array[String] - The associated instructor IDs.
	
	partnerIds: Array[String] - The associated partner IDs.
	
	photoUrl: Option[String] - A course photo.
	
	certificates: Array[CertificateType] - The available certificates
	
	description: String - A short description of the course.
	
	startDate: Option[DateTime] - The date the course was / will be launched. Note: this could be in the future, or in the past.
	
	workload: String - A short description of the workload.
	
	previewLink: Option[String] - If the course has enabled preview, this is the URL.
	
	specializations: Array[String] - The list of associated specializations for courses running on our v1 platform.
	
	s12nIds: Option[Array[S12nId]] - The related Specializations (S12ns) to this course for courses running on our v2 platform.
	
	domainTypes: Array[DomainType] - Domains (categories) and sub-domains associated with the course.
	
	categories: Array[String] - [Deprecated, see domains] The related categories in our old categories system.
	
	
# Add Kehan course fetch
just fetch kehan coursea data
