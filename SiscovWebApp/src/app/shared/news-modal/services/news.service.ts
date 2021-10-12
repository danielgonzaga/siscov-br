import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class NewsService {

  private readonly API = 'http://localhost:5000/'

  constructor(private http: HttpClient) { }

  listAllCountyNews(stateId, countyId) {
    return this.http.get<any>(this.API + 'state/' + stateId + '/county/' + countyId + '/variants');
  }

  listAllStateNews(stateId) {
    return this.http.get<any>(this.API + 'state/' + stateId + '/variants');
  }

  listAllRegionNews(regionId) {
    return this.http.get<any>(this.API + 'region/' + regionId + '/variants');
  }
}
