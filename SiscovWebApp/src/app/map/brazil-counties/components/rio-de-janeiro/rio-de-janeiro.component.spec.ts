import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RioDeJaneiroComponent } from './rio-de-janeiro.component';

describe('RioDeJaneiroComponent', () => {
  let component: RioDeJaneiroComponent;
  let fixture: ComponentFixture<RioDeJaneiroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RioDeJaneiroComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RioDeJaneiroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
