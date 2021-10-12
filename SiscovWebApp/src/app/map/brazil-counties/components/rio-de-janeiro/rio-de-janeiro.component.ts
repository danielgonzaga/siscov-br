import { Component, EventEmitter, OnInit, Output } from '@angular/core';


@Component({
  selector: 'app-rio-de-janeiro',
  templateUrl: './rio-de-janeiro.component.html',
  styleUrls: ['./rio-de-janeiro.component.css']
})
export class RioDeJaneiroComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
