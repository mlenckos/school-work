package shop.data;

/**
 * Implementation of Video interface.
 * @see Data
 */
final class VideoObj implements Video {
  private final String _title;
  private final int    _year;
  private final String _director;

  /**
   * Initialize all object attributes.
   * Title and director are "trimmed" to remove leading and final space.
   * @throws IllegalArgumentException if object invariant violated.
   */
  VideoObj(String title, int year, String director) {
	if(title==null||director==null||year>4999||year<1801) {
		throw new IllegalArgumentException();
	}
	if(title.trim().contentEquals("")||director.trim().equals("")){
		throw new IllegalArgumentException();
	}
    _title = title.trim();
    _director = director.trim();
    _year = year;
  }
/*
 * returns director string
 */
  public String director() {
    // todo - completed 
	return _director;
  }
  /*
   * returns title string
   */
  public String title() {
    // todo - completed
	  return _title;
  }
  /*
   * returns year string
   */
  public int year() {
    // todo - completed
	  return _year;
  }
/*
 * returns true/false depending on if its equal
 */
  public boolean equals(Object thatObject) {
    // todo - completed 
	  if (thatObject instanceof VideoObj) {
          VideoObj other = (VideoObj) thatObject;
          return (this._director.equals(other.director()) && this._title.equals(other.title()) && this._year == other.year());
	  }
	  return false;
  }
/*
 * returns hashcode
 */
  public int hashCode() {
    // todo - completed  
	  int result = 17;
      int prime = 37;
      result = prime * result + _title.hashCode();
      result = prime * result + _year;
      result = prime * result + _director.hashCode();
      return result;
  }
/*
 * returns compared to function
 */
  public int compareTo(Object thatObject) {
    // TODO  
	  VideoObj other = (VideoObj) thatObject;
      if (this._title.compareTo(other._title) != 0) {
              return this._title.compareTo(other._title);
      } 
      else {
    	  if (this._year != other._year) {
    		  return this._year - other._year;
          } 
    	  else {
    		  return this._director.compareTo(other._director);
          }
      }
  }
/*
 * returns to string
 */
  public String toString() {
    // TODO  
	  return _title + " (" + _year + ") : " + _director;
//	    StringBuffer buffer = new StringBuffer();
//	    buffer.append(_title);
//	    buffer.append("(");
//	    buffer.append(_year);
//	    buffer.append(") : ");
//	    buffer.append(_director);
//
//	    return buffer.toString();
  }
}
