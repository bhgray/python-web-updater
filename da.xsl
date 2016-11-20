<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">

<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
		<meta http-equiv="expires" content="Mon, 31 Dec 2001 23:59:59 GMT" />
		<link rel="stylesheet" href="../../styles/2col_leftNav.css" type="text/css" />
		<title>Teachopensource.org :: CompSci :: 
				<xsl:value-of select="da/course/key" />
		</title>
	</head>
	<body>
		<!--#include virtual="masthead.inc" -->
		<div id="content">
			<div id="breadCrumb">
				<a href="../index.shtml">Home</a> / 
				<a href="index.shtml">CS Home</a> / 
				<a href="../cs3syll.shtml" target="_self">
				<xsl:value-of select="da/course/key" /> 
				(Mods <xsl:value-of select="da/course/mods" />) Home</a> 
				/ Week of <xsl:value-of select="da/mon/date" />
			</div>
			<h2 id="pageName">Asssignment Details :: Week of 
				<xsl:value-of select="da/mon/date" />
			</h2> 
			<div class="story">
				<h3>Week Summary</h3>
				<p>Click on the day to advance to the details contained below.</p>
				<table width="500" border="1">
					<tr>
						<th width="100" scope="col">Day</th>
						<th width="188" scope="col">Classwork</th>
						<th width="190" scope="col">Homework</th>
					</tr>
					<tr>
						<td>
							<a href="#mon">Mon., <xsl:value-of select="da/mon/date" /><br />
								<xsl:if test="da/mon/@include = 1">
									(<xsl:value-of select="da/mon/letterDay" /> day)
								</xsl:if>
							</a>
						</td>
						<td>
							<xsl:choose>
								<xsl:when test="da/mon/@include = 1">
									<xsl:value-of select="da/mon/cw" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="da/mon/@include=2">
											<b>No Class Meeting</b>
										</xsl:when>
										<xsl:otherwise>
											<b>School Closed</b>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:otherwise>
							</xsl:choose>
						</td>
						<td>
							<xsl:choose>
								<xsl:when test="da/mon/@include = 1">
									<xsl:value-of select="da/mon/cw" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="da/mon/@include=2">
											<b>No Class Meeting</b>
										</xsl:when>
										<xsl:otherwise>
											<b>School Closed</b>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:otherwise>
							</xsl:choose>
						</td>
					</tr>
					<tr>
						<td>
							<a href="#tue">Tue., <xsl:value-of select="da/tue/date" /><br />
								<xsl:if test="da/tue/@include = 1">
									(<xsl:value-of select="da/tue/letterDay" /> day)
								</xsl:if>		
							</a>
						</td>
						<td>
							<xsl:choose>
								<xsl:when test="da/tue/@include = 1">
									<xsl:value-of select="da/tue/cw" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="da/tue/@include=2">
											<b>No Class Meeting</b>
										</xsl:when>
										<xsl:otherwise>
											<b>School Closed</b>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:otherwise>
							</xsl:choose>
						</td>
						<td>
							<xsl:choose>
								<xsl:when test="da/tue/@include = 1">
									<xsl:value-of select="da/mon/hw" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="da/tue/@include=2">
											<b>No Class Meeting</b>
										</xsl:when>
										<xsl:otherwise>
											<b>School Closed</b>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:otherwise>
							</xsl:choose>
						</td>
					</tr>
					<tr>
						<td>
							<a href="#wed">Wed., <xsl:value-of select="da/wed/date" /><br />
								<xsl:if test="da/wed/@include = 1">	
									(<xsl:value-of select="da/wed/letterDay" /> day)
								</xsl:if>	
							</a>
						</td>
						<td>
							<xsl:choose>
								<xsl:when test="da/wed/@include = 1">
									<xsl:value-of select="da/wed/cw" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="da/wed/@include=2">
											<b>No Class Meeting</b>
										</xsl:when>
										<xsl:otherwise>
											<b>School Closed</b>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:otherwise>
							</xsl:choose>
						</td>
						<td>
							<xsl:choose>
								<xsl:when test="da/wed/@include = 1">
									<xsl:value-of select="da/wed/hw" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="da/wed/@include=2">
											<b>No Class Meeting</b>
										</xsl:when>
										<xsl:otherwise>
											<b>School Closed</b>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:otherwise>
							</xsl:choose>
						</td>
					</tr>
					<tr>
						<td>
							<a href="#thu">Thu., <xsl:value-of select="da/thu/date" /><br />
								<xsl:if test="da/thu/@include = 1">
									(<xsl:value-of select="da/thu/letterDay" /> day)
								</xsl:if>
							</a>
						</td>
						<td>
							<xsl:choose>
								<xsl:when test="da/thu/@include = 1">
									<xsl:value-of select="da/thu/cw" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="da/thu/@include=2">
											<b>No Class Meeting</b>
										</xsl:when>
										<xsl:otherwise>
											<b>School Closed</b>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:otherwise>
							</xsl:choose>
						</td>
						<td>
							<xsl:choose>
								<xsl:when test="da/thu/@include = 1">
									<xsl:value-of select="da/thu/hw" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="da/thu/@include=2">
											<b>No Class Meeting</b>
										</xsl:when>
										<xsl:otherwise>
											<b>School Closed</b>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:otherwise>
							</xsl:choose>
						</td>
					</tr>
					<tr>
						<td>
							<a href="#fri">Fri., <xsl:value-of select="da/fri/date" /><br />
								<xsl:if test="da/fri/@include = 1">
									(<xsl:value-of select="da/fri/letterDay" /> day)
								</xsl:if>
							</a>
						</td>
						<td>
							<xsl:choose>
								<xsl:when test="da/fri/@include = 1">
									<xsl:value-of select="da/fri/cw" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="da/fri/@include=2">
											<b>No Class Meeting</b>
										</xsl:when>
										<xsl:otherwise>
											<b>School Closed</b>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:otherwise>
							</xsl:choose>
						</td>
						<td>
							<xsl:choose>
								<xsl:when test="da/fri/@include = 1">
									<xsl:value-of select="da/fri/hw" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:choose>
										<xsl:when test="da/fri/@include=2">
											<b>No Class Meeting</b>
										</xsl:when>
										<xsl:otherwise>
											<b>School Closed</b>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:otherwise>
							</xsl:choose>
						</td>
					</tr>
				</table>
			</div> <!-- END OF WEEK SUMMARY STORY -->			
			<div class="story"> 
				<h3><a name="mon">Mon., 
						<xsl:value-of select="da/mon/date" /><br />
						<xsl:if test="da/mon/@include = 1">
							(<xsl:value-of select="da/mon/letterDay" /> day)
						</xsl:if>
					</a>
				</h3>
			</div> <!-- END OF MONDAY DETAIL STORY -->
			<div class="story">
				<h3><a name="tue">Tue.,
						<xsl:value-of select="da/tue/date" />
						<xsl:if test="da/tue/@include = 1">
							(<xsl:value-of select="da/tue/letterDay" /> day)
						</xsl:if>				
					</a>
				</h3>
			</div> <!-- END OF TUESDAY DETAIL STORY -->
			<div class="story">
				<h3><a name="tue">Wed.,
						<xsl:value-of select="da/wed/date" />
						<xsl:if test="da/wed/@include = 1">
							(<xsl:value-of select="da/wed/letterDay" /> day)
						</xsl:if>				
					</a>
				</h3>
			</div> <!-- END OF WEDNESDAY DETAIL STORY -->
			<div class="story">
				<h3><a name="tue">Thu.,
						<xsl:value-of select="da/thu/date" />
						<xsl:if test="da/thu/@include = 1">
							(<xsl:value-of select="da/thu/letterDay" /> day)
						</xsl:if>				
					</a>
				</h3>
			</div> <!-- END OF THURSDAY DETAIL STORY -->
			<div class="story">
				<h3><a name="tue">Fri.,
						<xsl:value-of select="da/fri/date" />
						<xsl:if test="da/fri/@include = 1">
							(<xsl:value-of select="da/fri/letterDay" /> day)
						</xsl:if>				
					</a>
				</h3>
			</div> <!-- END OF FRIDAY  DETAIL STORY -->
		</div> <!-- END OF CONTENT -->

		<!--#include virtual="navbar.inc" -->
		<!--#include virtual="siteinfo.inc" -->
		<br /> 
		
	</body>
</html>
</xsl:template>
</xsl:stylesheet>