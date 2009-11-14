<?xml version="1.0" encoding="UTF-8"?>
<!--
 - Desc:    This file is part of the ecromedos Document Preparation System
 - Date:    2006/03/09
 - Author:  Tobias Koch (tkoch@ecromedos.net)
 - License: GNU General Public License, version 2
 - URL:     http://www.ecromedos.net
-->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<!--
 - This is there, to allow filtering of text with the pre-processor.
-->
<xsl:template match="span">
	<xsl:apply-templates/>
</xsl:template>

<!--
 - Sets a glossary section
-->
<xsl:template match="glossary">
	<!-- print links to index sections -->
	<xsl:if test="child::glsection[@name]">
		<div class="gllinks">
			<xsl:for-each select="glsection[@name]">
				<xsl:choose>
					<xsl:when test="dl/dt">
						<span class="gllink">
							<a href="#{generate-id()}" class="gllink">
								<xsl:value-of select="normalize-space(@name)"/>
							</a>
						</span>
					</xsl:when>
					<xsl:otherwise>
						<span class="glnolink">
							<xsl:value-of select="normalize-space(@name)"/>
						</span>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:for-each>
		</div>
		<hr class="glseparator"/>
	</xsl:if>
	<!-- render sections -->
	<xsl:for-each select="glsection[dl/dt]">
		<!-- section name, usually a
		letter from the alphabet -->
		<xsl:if test="@name">
			<h1 class="glsection">
				<a id="{generate-id()}" name="{generate-id()}"></a><xsl:value-of select="normalize-space(@name)"/>
			</h1>
		</xsl:if>
		<!-- render content -->
		<xsl:apply-templates/>
		<!-- horiz. rule -->
		<xsl:if test="position() != last()">
			<hr class="glseparator"/>
		</xsl:if>
	</xsl:for-each>
</xsl:template>

<!--
  - Entry point for printing the document.
-->
<xsl:template name="section.make">

	<!-- level of chunking -->
	<xsl:variable name="secsplitdepth">
		<xsl:call-template name="util.secsplitdepth"/>
	</xsl:variable>
	<!-- depth of numbering -->
	<xsl:variable name="secnumdepth">
		<xsl:call-template name="util.secnumdepth"/>
	</xsl:variable>

	<xsl:for-each select="head/following-sibling::*[
			not(substring(name(),1,4) = 'make') and
			not(name() = 'legal')
		]">
		<xsl:call-template name="section.print">
			<xsl:with-param name="curdepth" select="1"/>
			<xsl:with-param name="secsplitdepth" select="$secsplitdepth"/>
			<xsl:with-param name="secnumdepth" select="$secnumdepth"/>
		</xsl:call-template>
	</xsl:for-each>
</xsl:template>

<!--
 - Print the section heading. Calls 'section.anchor' to print the title
 - embedded in an anchor that can be referred and jumped to from the
 - table of contents.
-->
<xsl:template name="section.title">

	<xsl:param name="curdepth"/>
	<xsl:param name="secnumdepth"/>

	<!-- print numerical prefix -->
	<xsl:variable name="prefix">
		<xsl:choose>
			<xsl:when test="$secnumdepth >= $curdepth">
				<xsl:choose>
					<xsl:when test="
						name() = 'preface' or
						not(title) or
						ancestor-or-self::*[@tocentry='no']">
						<xsl:text></xsl:text>
					</xsl:when>
					<xsl:when test="self::part">
						<xsl:variable name="prefix">
							<xsl:call-template name="util.secprefix"/>
						</xsl:variable>
						<xsl:call-template name="i18n.print">
							<xsl:with-param name="key" select="'part'"/>
							<xsl:with-param name="number" select="$prefix"/>
						</xsl:call-template>
						<xsl:text> </xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:variable name="prefix">
							<xsl:call-template name="util.secprefix"/>
						</xsl:variable>
						<xsl:call-template name="i18n.print">
							<xsl:with-param name="key" select="'sectionnumber'"/>
							<xsl:with-param name="number" select="$prefix"/>
						</xsl:call-template>
						<xsl:text> </xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:text></xsl:text>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:variable>
	<!-- choose heading weight, depending on level -->
	<xsl:choose>
		<xsl:when test="not(title)">
			<h1><a id="{generate-id()}" name="{generate-id()}"></a>
				<xsl:choose>
					<xsl:when test="@title">
						<xsl:value-of select="normalize-space(@title)"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name="i18n.print">
							<xsl:with-param name="key" select="name()"/>
						</xsl:call-template>
					</xsl:otherwise>
				</xsl:choose>
			</h1>
		</xsl:when>
		<xsl:when test="$curdepth >= 5">
			<h4><a name="{generate-id()}" id="{generate-id()}"></a><xsl:value-of select="$prefix"/><xsl:apply-templates select="title"/></h4>		
		</xsl:when>
		<xsl:when test="$curdepth = 4">
			<h4><a name="{generate-id()}" id="{generate-id()}"></a><xsl:value-of select="$prefix"/><xsl:apply-templates select="title"/></h4>
		</xsl:when>
		<xsl:when test="$curdepth = 3">
			<h3><a name="{generate-id()}" id="{generate-id()}"></a><xsl:value-of select="$prefix"/><xsl:apply-templates select="title"/></h3>
		</xsl:when>
		<xsl:when test="$curdepth = 2">
			<h2><a name="{generate-id()}" id="{generate-id()}"></a><xsl:value-of select="$prefix"/><xsl:apply-templates select="title"/></h2>
		</xsl:when>
		<xsl:when test="$curdepth = 1">
			<h1><a name="{generate-id()}" id="{generate-id()}"></a><xsl:value-of select="$prefix"/><xsl:apply-templates select="title"/></h1>
		</xsl:when>
	</xsl:choose>
</xsl:template>

<!--
  - Print the contents of a section and call 'section.print' for
  - subsections.
-->
<xsl:template name="section.content">

	<xsl:param name="curdepth"/>
	<xsl:param name="secnumdepth"/>
	<xsl:param name="secsplitdepth"/>

	<!-- print title -->
	<xsl:call-template name="section.title">
		<xsl:with-param name="secnumdepth" select="$secnumdepth"/>
		<xsl:with-param name="curdepth" select="$curdepth"/>
	</xsl:call-template>
	<xsl:choose>
		<xsl:when test="not(title)">
			<xsl:apply-templates select="."/>
			<xsl:call-template name="footnote.text"/>
		</xsl:when>
		<xsl:otherwise>
			<!-- process section content -->
			<xsl:for-each select="
				child::*[not(
					name() = 'title' or
					name() = 'chapter' or
					name() = 'section' or
					name() = 'subsection' or
					name() = 'subsubsection'
				)]">
				<xsl:apply-templates select="."/>
			</xsl:for-each>
			<!-- set footnotes -->
			<xsl:call-template name="footnote.text"/>
			<!-- process subsections -->
			<xsl:for-each select="
				child::*[
					name() = 'chapter' or
					name() = 'section' or
					name() = 'subsection' or
					name() = 'subsubsection'
				]">
				<xsl:call-template name="section.print">
					<xsl:with-param name="curdepth" select="$curdepth + 1"/>
					<xsl:with-param name="secnumdepth" select="$secnumdepth"/>
					<xsl:with-param name="secsplitdepth" select="$secsplitdepth"/>
				</xsl:call-template>
			</xsl:for-each>
		</xsl:otherwise>
	</xsl:choose>
</xsl:template>

<!--
  - Returns name of file that contains the calling section.
-->
<xsl:template name="section.file">
	<xsl:choose>
		<xsl:when test="name() = 'preface'">
			<xsl:text>preface</xsl:text>
			<xsl:number count="preface"/>
			<xsl:text>.html</xsl:text>
		</xsl:when>
		<xsl:when test="name() = 'index'">
			<xsl:text>index</xsl:text>
			<xsl:number count="index"/>
			<xsl:text>.html</xsl:text>
		</xsl:when>
		<xsl:when test="not(title)">
			<xsl:value-of select="name()"/><xsl:text>.html</xsl:text>
		</xsl:when>
		<xsl:otherwise>
			<xsl:value-of select="name()"/>
			<xsl:call-template name="util.secprefix"/>
			<xsl:text>.html</xsl:text>
		</xsl:otherwise>
	</xsl:choose>
</xsl:template>

<!--
  - Recursive template that takes care of splitting the document in
  - multiple output files and printing section contents.
-->
<xsl:template name="section.print">
	
	<xsl:param name="secsplitdepth"/>
	<xsl:param name="curdepth"/>
	<xsl:param name="secnumdepth"/>
	
	<xsl:choose>
		<!-- put section in separate file -->
		<xsl:when test="$secsplitdepth >= $curdepth">
			<xsl:variable name="filename">
				<xsl:call-template name="section.file"/>
			</xsl:variable>
			<!-- output to separate file -->
			<xsl:document href="{$filename}" method="xml" indent="no" encoding="UTF-8"
			doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
			doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"
			omit-xml-declaration="yes">
				<html>
					<head>
						<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
						<meta name="generator" content="{$global.version}"/>
						
						<!-- insert CSS -->
						<link rel="stylesheet" type="text/css" href="style.css"/>

						<!-- title -->
						<title><xsl:call-template name="util.print.title"/></title>

						<!-- javascript -->
						<xsl:if test="//marginal">
							<!-- alignment of marginals -->
							<xsl:call-template name="marginal.script">
								<xsl:with-param name="curdepth" select="$curdepth"/>
								<xsl:with-param name="secsplitdepth" select="$secsplitdepth"/>
							</xsl:call-template>
						</xsl:if>
					</head>
					<body>

						<!-- top navigation bar -->
						<xsl:call-template name="xhtml.pagehead">
							<xsl:with-param name="secsplitdepth" select="$secsplitdepth"/>
							<xsl:with-param name="curdepth" select="$curdepth"/>
							<xsl:with-param name="secnumdepth" select="$secnumdepth"/>
						</xsl:call-template>

						<!-- set content -->
						<div id="content">
							<table border="0" cellspacing="0" cellpadding="0" class="content">
								<tr>
									<!-- body -->
									<td class="textbody">

										<!-- set content -->
										<xsl:call-template name="section.content">
											<xsl:with-param name="secsplitdepth" select="$secsplitdepth"/>
											<xsl:with-param name="curdepth" select="$curdepth"/>
											<xsl:with-param name="secnumdepth" select="$secnumdepth"/>
										</xsl:call-template>

									</td>
									<!-- margin -->
									<xsl:if test="//marginal">
										<td class="margin">

											<!-- make marginal notes -->
											<xsl:call-template name="marginal.text">
												<xsl:with-param name="curdepth" select="1"/>
												<xsl:with-param name="secsplitdepth" select="$secsplitdepth"/>
											</xsl:call-template>

											<!-- IE won't show border if margin is empty -->
											<xsl:text disable-output-escaping="yes">&amp;nbsp;</xsl:text>

										</td>
									</xsl:if>
								</tr>
							</table>
						</div>

						<!-- bottom navigation bar -->
						<xsl:call-template name="xhtml.pagefoot">
							<xsl:with-param name="secsplitdepth" select="$secsplitdepth"/>
							<xsl:with-param name="curdepth" select="$curdepth"/>
							<xsl:with-param name="secnumdepth" select="$secnumdepth"/>
						</xsl:call-template>

					</body>
				</html>
			</xsl:document>
		</xsl:when>
		<!-- put section in same file -->
		<xsl:otherwise>
			<xsl:call-template name="section.content">
				<xsl:with-param name="secsplitdepth" select="$secsplitdepth"/>
				<xsl:with-param name="curdepth" select="$curdepth"/>
				<xsl:with-param name="secnumdepth" select="$secnumdepth"/>
			</xsl:call-template>
		</xsl:otherwise>
	</xsl:choose>
</xsl:template>

<!--
  - A minisection is an odd kind of section. It does not have a fixed place in
  - the section hierarchy. Instead, it can occur pretty much anywhere and only
  - serves the purpose of having a series of titled paragraphs. Minisections
  - are not numbered!
-->
<xsl:template match="minisection">
	<h5>
		<xsl:apply-templates select="title"/>
	</h5>
	<xsl:apply-templates select="title/following-sibling::*"/>
</xsl:template>

</xsl:stylesheet>
