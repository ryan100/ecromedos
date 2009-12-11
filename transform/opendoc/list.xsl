<?xml version="1.0" encoding="UTF-8"?>
<!--
 - Desc:    This file is part of the ecromedos Document Preparation System
 - Author:  Tobias Koch (tkoch@ecromedos.net)
 - License: GNU General Public License, version 2
 - URL:     http://www.ecromedos.net
 - Date:    2009/11/15
-->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<!--
  - Process simple bullet lists.
-->
<xsl:template match="ul">
	<ul>
		<xsl:apply-templates/>
	</ul>
</xsl:template>

<!--
  - Handle enumerated lists.
-->
<xsl:template match="ol">
	<xsl:variable name="num_ancestors">
		<xsl:value-of select="count(ancestor::ol)"/>
	</xsl:variable>
	<xsl:variable name="style">
		<xsl:choose>
			<xsl:when test="@type">
				<xsl:value-of select="@type"/>
			</xsl:when>
			<xsl:when test="$num_ancestors = 3">
				<xsl:text>A</xsl:text>
			</xsl:when>
			<xsl:when test="$num_ancestors = 2">
				<xsl:text>i</xsl:text>
			</xsl:when>
			<xsl:when test="$num_ancestors = 1">
				<xsl:text>a</xsl:text>
			</xsl:when>
			<xsl:otherwise>
				<!-- empty -->
			</xsl:otherwise>
		</xsl:choose>
	</xsl:variable>
	<ol>
		<xsl:if test="$style != ''">
			<xsl:attribute name="type">
				<xsl:value-of select="$style"/>
			</xsl:attribute>
		</xsl:if>
		<xsl:apply-templates/>
	</ol>
</xsl:template>

<!--
  - Set a list item in bullet/enumerated lists.
-->
<xsl:template match="li">
	<li>
		<xsl:apply-templates/>
	</li>
</xsl:template>

<!--
  - Process a glossary-type list.
-->
<xsl:template match="dl">
	<dl>
		<xsl:apply-templates select="dt|dd"/>
	</dl>
</xsl:template>

<!--
  - Set an item in glossary lists...
-->
<xsl:template match="dt">
	<dt>
		<b><xsl:apply-templates/></b>
	</dt>
</xsl:template>

<!--
  - ...and its definition
-->
<xsl:template match="dd">
	<dd>
		<xsl:apply-templates/>
	</dd>
</xsl:template>

<!--
  - Return item prefix for 'ref' statements
-->
<xsl:template name="listitem.prefix">
	<xsl:variable name="num_ancestors">
		<xsl:value-of select="count(ancestor::ol)"/>
	</xsl:variable>
	<xsl:choose>
		<xsl:when test="ancestor::ol[1]/@type">
			<xsl:value-of select="ancestor::ol[1]/@type"/>
		</xsl:when>
		<xsl:when test="$num_ancestors = 4">
			<xsl:number count="li" format="A"/>
		</xsl:when>
		<xsl:when test="$num_ancestors = 3">
			<xsl:number count="li" format="i"/>
		</xsl:when>
		<xsl:when test="$num_ancestors = 2">
			<xsl:number count="li" format="a"/>
		</xsl:when>
		<xsl:otherwise>
			<xsl:number count="li"/>
		</xsl:otherwise>
	</xsl:choose>
</xsl:template>

</xsl:stylesheet>
